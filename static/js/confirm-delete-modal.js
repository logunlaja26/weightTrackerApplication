function showConfirmDeleteModal(id) {
   document.getElementById('confirm-delete-modal').style.display = "block";

   document.getElementById('confirm-delete-modal-weight-entry-id').value = id;
 }

function closeConfirmDeleteModal(){
  document.getElementById('confirm-delete-modal').style.display = "none";

}
