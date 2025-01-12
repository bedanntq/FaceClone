// script.js
//Đoạn mã JavaScript dùng để xử lý khi gửi bình luận
// document.getElementById('comment-form').addEventListener('submit', function (e) {
//     e.preventDefault(); // Ngăn form submit thông thường

//     const postId = document.getElementById('post_id').value;
//     const content = document.getElementById('content').value;
//     const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

//     fetch('/add_comment_test/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrfToken
//         },
//         body: JSON.stringify({ post_id: postId, content: content })
//     })
//     .then(response => response.json())
//     .then(data => {
//         if (data.success) {
//             // Thêm bình luận mới vào danh sách
//             const commentList = document.getElementById('comment-list');
//             const newComment = document.createElement('li');
//             newComment.innerHTML = `
//                 <strong>${data.comment.author}</strong>: ${data.comment.content}
//                 <small>(${data.comment.date_created})</small>
//             `;
//             commentList.appendChild(newComment);

//             // Xóa nội dung form
//             document.getElementById('content').value = '';
//         } else {
//             alert('Error: ' + data.error);
//         }
//     })
//     .catch(error => console.error('Error:', error));    
// });
//------------------------------------------------------------------------------------------------
// Hàm tải lại danh sách bình luận
function loadComments(postId) {
    const commentList = document.getElementById('comment-list');
    const url = `/get_comments/${postId}/`; // URL API để lấy bình luận

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.comments) {
                // Xóa các bình luận cũ
                commentList.innerHTML = '';

                // Thêm bình luận mới
                data.comments.forEach(comment => {
                    const commentItem = document.createElement('li');
                    commentItem.innerHTML = `
                        <strong>${comment.author}</strong>: ${comment.content}
                        <small>(${comment.date_created})</small>
                    `;
                    commentList.appendChild(commentItem);
                });
            } else {
                console.error('Failed to load comments.');
            }
        })
        .catch(error => console.error('Error:', error));
}

// Gọi hàm loadComments khi tải trang
document.addEventListener('DOMContentLoaded', function () {
    const postId = document.getElementById('post_id').value;
    loadComments(postId);
});

// Thêm bình luận mới
document.getElementById('comment-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const postId = document.getElementById('post_id').value;
    const content = document.getElementById('content').value;
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch('/add_comment_test/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ post_id: postId, content: content })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Sau khi thêm bình luận, tải lại danh sách bình luận
            loadComments(postId);
            document.getElementById('content').value = ''; // Xóa nội dung form
        } else {
            alert('Error: ' + data.error);
        }
    })
    .catch(error => console.error('Error:', error));
});
