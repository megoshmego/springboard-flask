let boggle_timer = 60
let word_match = new Set()
let $form = $(".form-group")
$form.on("submit", handleForm)
$("#reload").on("click", function(){ location.reload()})



// timer
let tick = setInterval(function () {
    $timer = $("#timer");
    if (boggle_timer === 0) {
        clearInterval(tick)
        $("#input").prop("disabled", true)
        $form.prop("disabled", true)
        endGame(parseInt($('#score').html()))
    }
    $timer.text(boggle_timer--)
}, 1000)

async function makeRequest(url, verb, data) {
    let response
    switch (verb) {
        case "GET":
            response = await axios.get(url)
            return response
        case "POST":
            response = await axios.post(url, data)
            return response
    }
}

function updateBoard(result) {
    switch (result) {
        // response
        case "ok":
            stat_refresh()
            break;
        case "not-on-board":
            $response.html("Not on board")
            break;
        case "not-word":
            $response.html("Not a word")
            break;
}
}


// get latest stats on matching words and score 

function stat_refresh() {
    $response.html("Found a word!")
    if (!word_match.has($word)) {
        word_match.add($word)
        $words = $("#words");
        $words.empty();
        word_match.forEach(word => {
            btn = $(`<button class="btn m-1 p-1">${word}</button>`)
            $words.append(btn)
        })
        
        // updateScore
        $('#score').html(parseInt($('#score').html(), 10)+$word.length)
    }
    else {
        $response.html("Word already found!")
            setTimeout(function () {
                cleanUp()
            },1500)
            return
    }
}

       
//   ########################################################
async function endGame(score){
    // send a request for /update-HighScore with the score data
    let url = `http://127.0.0.1:5000/update-HighScore`
    let data = { score: score }
    const response = await makeRequest(url,"POST", data)
    if (response.status !== 201) {
        console.log(`Error : ${response.status}. Message: ${response.statusText}`)
    }
    else {
        console.log(response)


  
        $("#top_score ").html(response.data.top_score )
        $("#next_game").html(response.data.next_game)
    }
}
//   ########################################################
function cleanUp() {
        $word_guesses.empty(),
        $response.empty()
        $form.trigger("reset")
}
// ******************************************************************************************************************
async function handleForm(evt) {
    evt.preventDefault()
    $word = $("#input").val()
    // validate
    if ($word !== "") {
        url = `http://127.0.0.1:5000/check-word?word=${$word}`;
        const response = await makeRequest(url, "GET")
        if (response.status !== 200) {
            console.log(`ERROR checkWord: ${response.status} ${response.statusText}`);
            return;
        }
        else {
            $word_guesses = $("#word_guessed")
            $response = $("#response")
            // add word guessed
            $word_guesses.fadeIn("slow", function () {
                $word_guesses.html($word)
            })
            let result = response.data.result
            updateBoard(result)
            setTimeout(function () {
                cleanUp()
            }, 1000)
        }
    }
}
