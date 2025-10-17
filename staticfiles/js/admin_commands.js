
addEventListener("DOMContentLoaded", (event) => {
    const deleteCategoryModal = new bootstrap.Modal(document.getElementById("deleteCategoryModal"));
    const deleteCategoryButtons = document.getElementsByClassName("btn-delete");

    const deleteMediaModal = new bootstrap.Modal(document.getElementById("deleteMediaModal"));
    const deleteMediaButtons = document.getElementsByClassName("btn-warning");

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
    for (let button of deleteCategoryButtons) {
        console.log("Delete button is "+button);
        button.addEventListener("click", (e) => {
        console.log("button is clicked");
        let categoryid = e.target.getAttribute("data-category_id");
        console.log(`e.target is ${e.target} and categoryid is ${categoryid}`);
        deleteCategoryConfirm.href = `/delete_category/${categoryid}`;
        deleteCategoryModal.show();
    });
    }

    for (let button of deleteMediaButtons) {
        console.log("Delete button is "+button);
        button.addEventListener("click", (e) => {
        console.log("button is clicked");
        let mediaid = e.target.getAttribute("data-media_id");
        console.log(`e.target is ${e.target} and mediaid is ${mediaid}`);
        deleteMediaConfirm.href = `/delete_media/${mediaid}`;
        deleteMediaModal.show();
    });
    }

})
