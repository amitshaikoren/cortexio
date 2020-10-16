
var slideIndex = 0;
var snapshotsURL = apiURL + "/users/" + userID + "/snapshots";
var snapshotImageURL = [];
var COLOR = 0;
var DEPTH = 1;
var DATE = 2;
var currColorImageURL;
var currDepthImageURL;
var currDatetime;

async function getSnapshotIDs(){
    await $.get(snapshotsURL, function(data){
        data.sort(compareSnapshotsByDatetime);
        for(var i=0;i<data.length;i++){
            var snapshot = data[i];
            var colorImageURL = snapshotsURL + "/" + snapshot.snapshot_id + "/color_image/data";
            var depthImageURL = snapshotsURL + "/" + snapshot.snapshot_id + "/depth_image/data";
            var datetime = snapshot.datetime;
            snapshotImageURL.push(
                [colorImageURL, depthImageURL, datetime]
            );
        };
    });
}


function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {

  var x = document.getElementsByClassName("myColorImageSlides");
  if (n > snapshotImageURL.length) {slideIndex = 0;}
  if (n < 0) {slideIndex = snapshotImagePaths.length-1;}


  currColorImageURL = snapshotImageURL[slideIndex][COLOR];
  currDepthImageURL = snapshotImageURL[slideIndex][DEPTH];
  currDatetime = snapshotImageURL[slideIndex][DATE];

  addUserSnapshotImages();
}

function getTimestampFromEpoch(time){
    return new Date(time);
}


async function addUserSnapshotImages(){

    var colorImageElement = document.getElementById("color_image_slide");
    var depthImageElement = document.getElementById("depth_image_slide");


    await $.get(snapshotsURL, function(data){
        data.sort(compareSnapshotsByDatetime);

            var linesToAddColorImage = `
                <img src= ${currColorImageURL}  style="width:100%">
                  <div class="w3-display-bottomleft w3-large w3-container w3-padding-16 w3-black">
                      ${getTimestampFromEpoch(currDatetime)}
                  </div>`;

            var linesToAddDepthImage = `
                <img src= ${currDepthImageURL}  style="width:100%">
                  <div class="w3-display-bottomleft w3-large w3-container w3-padding-16 w3-black">
                      ${getTimestampFromEpoch(currDatetime)}
                  </div>`;

            colorImageElement.innerHTML = linesToAddColorImage;
            depthImageElement.innerHTML = linesToAddDepthImage;
    });

}

function compareSnapshotsByDatetime(snapshot1, snapshot2){
    if (snapshot1.datetime < snapshot2.datetime) {return -1;}
    if (snapshot2.datetime < snapshot1.datetime) {return 1;}
    return 0;
}




async function drawChart() {
        var graphData = [];

        //feelings graph over time
        var graph = new google.visualization.DataTable();
        graph.addColumn('number', 'Time since epoch');



        var feeling_types;

        await $.get(snapshotsURL, function(data){
            feeling_types = Object.keys(data[0].results.feelings);

            data.sort(compareSnapshotsByDatetime);
            for(var i = 0; i<data.length; i++){

                var feelings_data = data[i].results.feelings;
                if(feelings_data==null){
                    continue;
                }
                var snapshot_data = [data[i].datetime];

                //adding data to snapshot_data

                feeling_types.forEach(function(feeling_type){
                    snapshot_data.push(feelings_data[feeling_type]);
                });

                //adding columns to graph
                graphData.push(snapshot_data);
            }
            feeling_types.forEach(function(feeling_type){
                graph.addColumn('number', feeling_type);
            });
      });
      console.log("exits draw chart get");

      graph.addRows(graphData);

      var options = {
        chart: {
          title: "Feelings of user " + userID + " over time.",
          subtitle: 'in seconds'
        },
        width: 900,
        height: 500,
        axes: {
        x: {
           0: {side: 'top'}
        }},
        hAxis: {format: 'decimal'}
      };

      var chart = new google.charts.Line(document.getElementById('line_top_x'));
      chart.draw(graph, google.charts.Line.convertOptions(options));

}

async function showImages(){
    await getSnapshotIDs();
    await showDivs(slideIndex);
}

