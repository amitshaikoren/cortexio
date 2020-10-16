var usersByIDName;
var usersURL = apiURL + "/users"



async function getUsers(){
    await $.get(usersURL, function(users){
        usersByIDName = users;
        usersByIDName.forEach(function(signifier){
            signifier[1] = signifier[1].toUpperCase()
        });
    });
}

function search() {
  var input = document.getElementById("search");
  searchInput = input.value.toUpperCase();
  usersByIDName.forEach(function(signifier){
    var userID = signifier[0];
    var userName = signifier[1];
    if(searchInput == userID ||
       searchInput == userName
       ){
           window.location.href = guiURL + "/user_page/" + userID;
       }
    else{window.location.href = guiURL + "/404_user_not_found";}

  });
}
function enterSearch(){
    if(event.key == 'Enter'){
        search();
    }

}


async function addUsersCards(){
    var cards = document.getElementById("cards")

    usersByIDName.forEach(async function(signifier){
        var userID = signifier[0];
        var userName = signifier[1];
        var userURL = usersURL + '/' + userID;

        var userBirthday;
        var userGender;

        await $.get(userURL, function(data){
            userBirthday = data.birthday;
            userGender = data.gender;
        });

        linesToAdd = `
        	<div class="content">
              <div class="card" onclick="changeAddress(${userID})" style="cursor: pointer">
                <div class="card__side card__side--front">
                  <!-- Front Content -->
                  <div class="card__cont">
                    <span class="orange">var&nbsp</span>user =&nbsp<span class ="green">"${userName}"</span>;
                  </div>
                </div>
                <div class="card__side card__side--back">
                  <!-- Back Content -->
                  <div class="card__cta">
                    <p><span class="purple">const</span> aboutMe <span class="cyan">=</span> {
                      <br />
                      <span class="space red">name</span>
                      <span class="cyan">:&nbsp</span><span class ="green">"${userName}"</span>,
                      <br/>
                      <span class="space red">birthday</span>
                      <span class="cyan">:&nbsp</span> <span class="green">"${userBirthday}"</span>,
                      <br/>
                      <span class="space red">gender</span>
                      <span class="cyan">:</span>
                      ${userGender},
                      <br/>
                      <span class="space red">userID</span><span class="cyan">:&nbsp</span>${userID}
                      <br/>
                      };
                    </p>
                  </div>
                </div>
              </div>
            </div>
           </div>
        `;

        cards.innerHTML += linesToAdd;
    })
}

async function getPageData(){
    await getUsers();
    await addUsersCards();
}

function changeAddress(userID){
    window.location.href = guiURL + "/user_page/" + userID;
}