document.addEventListener("DOMContentLoaded", function () {
    const commentBtn = document.getElementById("commentBtn");
    const commentForm = document.getElementById("commentForm");
    const commentSection = document.getElementById("commentSection");

    if (commentBtn && commentForm) {
        commentBtn.addEventListener("click", function () {
            const postId = commentForm.dataset.postId;
            const commentContent = document.getElementById("content").value;
            const csrfToken = document.querySelector("input[name=csrfmiddlewaretoken]").value;

            fetch(`/add_comment/${postId}/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: new URLSearchParams({
                    content: commentContent,
                    csrfmiddlewaretoken: csrfToken,
                }),
            })
                .then((response) => response.json())
                .then((data) => {
                    if (data.comment) {
                        const newComment = `
                            <div>
                                <strong>${data.comment.author}</strong>: ${data.comment.content}
                                <small>${data.comment.created_at}</small>
                            </div>`;
                        commentSection.innerHTML += newComment;
                        document.getElementById("content").value = ""; // Xóa nội dung sau khi gửi
                    } else if (data.error) {
                        alert("Error: " + data.error);
                    }
                })
                .catch((error) => {
                    console.error("Error:", error);
                    alert("Failed to add comment.");
                });
        });
    }
});
