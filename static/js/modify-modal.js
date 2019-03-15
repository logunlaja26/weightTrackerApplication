function openForm(id, date, weight) {
   document.getElementById('myForm').style.display = "block";

   // assign id to serve record data from the server side
   document.getElementById('id').value = id;
   // assign the weight input to date
   document.getElementById('date').value = date;
   // document.getElementById('date').value = "01-22-2018";
   // assign the date input to weight
   document.getElementById('weight').value = weight;
}

function closeForm() {
    document.getElementById('myForm').style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  var modal = document.getElementById('myForm');
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// When the user clicks on <span> (x), close the modal
var span = document.getElementsByClassName("close")[0];
span.onclick = function() {
  var modal = document.getElementById('myForm');
  modal.style.display = "none";
}
