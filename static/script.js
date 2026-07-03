async function generateScript() {

    const topic = document.getElementById("topic").value;

    if(topic===""){
        alert("Please enter a topic.");
        return;
    }

    document.getElementById("loading").style.display="block";
    document.getElementById("output").textContent="";
    document.getElementById("status").textContent="🧠 Generating Script...";

    const bar=document.getElementById("bar");
    bar.style.width="10%";

    const response=await fetch("/generate",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            topic:topic
        })
    });

    bar.style.width="70%";

    const data=await response.json();

    bar.style.width="100%";

    document.getElementById("status").textContent="✅ Completed";

    let text = data.script + "\n\n🎬 Scenes\n\n";

data.scenes.forEach((scene, index) => {
    text += `Scene ${index + 1}\n${scene}\n\n`;
});

document.getElementById("output").textContent = text;

    setTimeout(()=>{
        document.getElementById("loading").style.display="none";
        bar.style.width="0%";
    },1000);

}
0


