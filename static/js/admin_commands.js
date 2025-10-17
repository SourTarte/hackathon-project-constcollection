
addEventListener("DOMContentLoaded", (event) => {
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");

    /**
    * Initializes deletion functionality for the provided delete buttons.
    * 
    * For each button in the `deleteButtons` collection:
    * - Retrieves the associated comment's ID upon click.
    * - Updates the `deleteConfirm` link's href to point to the 
    * deletion endpoint for the specific comment.
    * - Displays a confirmation modal (`deleteModal`) to prompt 
    * the user for confirmation before deletion.
    */
    console.log(window.location.href)
    for (let button of deleteButtons) {
        console.log("Delete button is "+button);
        button.addEventListener("click", (e) => {
        console.log("button is clicked");
        let categoryid = e.target.getAttribute("data-category_id");
        console.log(`e.target is ${e.target} and categoryid is ${categoryid}`);
        deleteConfirm.href = `/delete_category/${categoryid}`;
        deleteModal.show();
    });
    }

})
