const nama = "Hansen indra";
// const itu konstanta yang gaada nilainya dan gabisa diubah nilainya kalo engga manual
let usia = 17;
// let itu variabel buat angka

let biodata = document.getElementById('biodata');

function generateBiodata() {
    let generasi;

// di atas ini ^^, generasi ini bakal punya nilai pas kondisi dibawah terpenuhi
  if(usia > 10 && usia < 18) {
     generasi = "Generasi Remaja";
  } 
  else if (usia >= 18) {
    generasi = "Generasi Dewasa"; 
  } 
  else if (usia > 4 && usia < 11) {
    generasi = "Generasi Muda";
  }
  else {
    generasi = "Generasi Bayi";
  }
  
  return biodata.innerHTML = generasi;
}



console.log(nama);
console.log(usia);
console.log (`Nama saya adalah`,nama,`dan saya berumur ${usia} tahun`);
generateBiodata();
