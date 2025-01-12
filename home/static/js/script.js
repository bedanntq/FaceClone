// script.js
// document.querySelector('.post-box button').addEventListener('click', () => {
//     const textarea = document.querySelector('.post-box textarea');
//     const postContent = textarea.value.trim();
//     if (postContent) {
//         const postsContainer = document.querySelector('.posts');
//         const newPost = document.createElement('div');
//         newPost.classList.add('post');
//         newPost.innerHTML = `<p><strong>You:</strong> ${postContent}</p>`;
//         postsContainer.prepend(newPost);
//         textarea.value = '';
//     }
// });
function openModal(postId, imageUrl, content, author) {
    // Hiển thị modal
    const modal = document.getElementById('imageModal');
    modal.style.display = 'flex';

    // Gắn dữ liệu vào modal
    document.getElementById('modalImage').src = imageUrl;
    document.getElementById('modalContent').textContent = content;
    document.getElementById('modalAuthor').textContent = "Posted by: " + author;
}

function closeModal() {
    // Ẩn modal
    const modal = document.getElementById('imageModal');
    modal.style.display = 'none';
}
