export function loadMiams(){
    let miams = [];
    fetch('miam.json')
        .then(response => response.json())
        .then(data => {
            miams = data.fruits_et_legumes;
            console.log(miams);
        });
    console.log(miams);
    return miams;
}