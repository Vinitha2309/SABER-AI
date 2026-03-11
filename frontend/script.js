function predictStress(){

let study=document.getElementById("study").value
let sleep=document.getElementById("sleep").value
let deadlines=document.getElementById("deadlines").value
let typing=document.getElementById("typing").value

let data={
study_hours:study,
sleep_hours:sleep,
deadlines:deadlines,
typing_speed:typing
}

fetch("http://127.0.0.1:5000/predict_stress",{

method:"POST",
headers:{
"Content-Type":"application/json"
},

body:JSON.stringify(data)

})

.then(response=>response.json())
.then(result=>{

let plan=result.recommended_plan

let text="Stress Level: "+result.stress_level+"<br><br>Recommended Plan:<br>"

for(let key in plan){

text+=key+" : "+plan[key]+"<br>"

}

document.getElementById("stressResult").innerHTML=text

})

}


function uploadVoice(){

let file=document.getElementById("voiceFile").files[0]

let formData=new FormData()

formData.append("file",file)

fetch("http://127.0.0.1:5000/voice_emotion",{

method:"POST",
body:formData

})

.then(response=>response.json())
.then(result=>{

document.getElementById("voiceResult").innerHTML=
"Detected Emotion: "+result.emotion

})

}
