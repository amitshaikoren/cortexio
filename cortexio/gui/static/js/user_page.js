var apiURL = "http://127.0.0.1:7000";

var slideIndex = 1;

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("myColorImageSlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";
  }
  x[slideIndex-1].style.display = "block";


  var z = document.getElementsByClassName("myDepthImageSlides");
  if (n > z.length) {slideIndex = 1}
  if (n < 1) {slideIndex = z.length}
  for (i = 0; i < z.length; i++) {1
     z[i].style.display = "none";
  }
  z[slideIndex-1].style.display = "block";
}



function getTimestampBySnapshotID(snapshotID, userID){
    var user_snapshot_url = apiURL + "/users/" + userID + "/snapshots";
    var d = new Date(0)
    d.setUTCSeconds()

    $.get(user_snapshot_url, function(data){
        for(var i=0; i<data.length; i++){
            if(data[i].snapshot_id == snapshotID){
                d.setUTCSeconds(data[i].datetime)
                return d
            }
        }
    });
}

function getColorImagePathBySnapshotID(snapshotID, userID){
    var user_snapshot_url = apiURL + "/users/" + userID + "/snapshots";

    $.get(user_snapshot_url, function(data) {
        for(var i; i<data.length; i++){
            if(data[i].snapshot_id == snapshotID){
                return data[i].color_image.data_path
            }
        }
    })

}

function getDepthImagePathBySnapshotID(snapshotID, userID){
    var user_snapshot_url = apiURL + "/users/" + userID + "/snapshots";

    $.get(user_snapshot_url, function(data) {
        for(var i; i<data.length; i++){
            if(data[i].snapshot_id == snapshotID){
                return data[i].depth_image.data_path
            }
        }
    })

}

async function addUserSnapshotImages(apiURL, userID){
    var user_snapshot_url = apiURL + "/users/" + userID + "/snapshots";
    var colorImageElement = document.getElementById("snapshot_color_images");
    var depthImageElement = document.getElementById("snapshot_depth_images");
    var d = new Date(0)


    await $.get(user_snapshot_url, function(data){
        // get snapshot image paths and add images to html
        for(var i=0; i<data.length; i++){
            var snapshotColorImgURL = apiURL + "users/" + userID + "/snapshots/" + data[i].snapshot_id + "/color_image/data"
            var snapshotDepthImgURL = apiURL + "users/" + userID + "/snapshots/" + data[i].snapshot_id + "/depth_image/data"
            d.setUTCSeconds(data[i].datetime);
            var snapshotTimestamp = d;

            var linesToAddColorImage =
                `<div class="w3-display-container myColorImageSlides center">
                  <img src=` + snapshotColorImgURL + ` style="width:100%">
                  <div class="w3-display-bottomleft w3-large w3-container w3-padding-16 w3-black">
                    ` + snapshotTimestamp + `
                  </div>
                </div>`;

            var linesToAddDepthImage =
                `<div class="w3-display-container myDepthImageSlides center">
                  <img src=` + snapshotDepthImgURL + ` style="width:100%">
                  <div class="w3-display-bottomleft w3-large w3-container w3-padding-16 w3-black">
                    ` + snapshotTimestamp + `
                  </div>
                </div>`;

            colorImageElement.innerHTML += linesToAddColorImage;
            depthImageElement.innerHTML += linesToAddDepthImage;
    }});



}


