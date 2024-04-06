let score = 0;
let score_text = document.getElementById("score").innerText;
function nextQuestion(currentQuestionId, nextQuestionId, questionNumber) {
    const currentQuestion = document.getElementById(currentQuestionId);
    const selectedAnswer = currentQuestion.querySelector('input[type="radio"]:checked');
    if (selectedAnswer == null) {
        alert("select your answer");
        return;
    }
    if (questionNumber == 15) {
        checkAnswer(currentQuestion, questionNumber);
        showResult();
        sendScore(score)
        return;
    } else if (questionNumber <= 14) {
        const currentQuestion = document.getElementById(currentQuestionId);
        const nextQuestion = document.getElementById(nextQuestionId);
        checkAnswer(currentQuestion, questionNumber);
        currentQuestion.classList.remove('active');
        nextQuestion.classList.add('active');
    }
}


function checkAnswer(currentQuestion, questionNumber) {
    const selectedAnswer = currentQuestion.querySelector('input[type="radio"]:checked');
    if (selectedAnswer) {
        const correctAnswer = getCorrectAnswer(parseInt(questionNumber)); // หาคำตอบที่ถูกต้อง
        if (score >= 15) {
            return;
        }
        if (selectedAnswer.value === correctAnswer) {
            score += 1; // เพิ่มคะแนนเมื่อตอบถูก
            console.log(score);
        }
    }
}

function getCorrectAnswer(questionNumber) {
    switch (questionNumber) {
        case 1:
            return 'ก';
        case 2:
            return 'จ';
        case 3:
            return 'จ';
        case 4:
            return 'ข';
        case 5:
            return 'จ';
        case 6:
            return 'ข';
        case 7:
            return 'ข';
        case 8:
            return 'ก';
        case 9:
            return 'จ';
        case 10:
            return 'ง';
        case 11:
            return 'ก';
        case 12:
            return 'ง';
        case 13:
            return 'ข';
        case 14:
            return 'จ';
        case 15:
            return 'ง';
        default:
            return '';
    }
}

function showResult() {
    const show_score = document.getElementById("result");
    show_score.style.display = "block";
    document.getElementById("score").innerHTML = score + "";
}

const token = localStorage.getItem('token')
if (!token) {

    window.location.href = "{% url 'login' %}";
}