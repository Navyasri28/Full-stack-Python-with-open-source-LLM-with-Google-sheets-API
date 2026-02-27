document.addEventListener('DOMContentLoaded', () => {
    const userForm = document.getElementById('user-form');
    const userBody = document.getElementById('user-body');
    const refreshBtn = document.getElementById('refresh-btn');
    const loader = document.getElementById('loader');
    const emptyState = document.getElementById('empty-state');
    const notification = document.getElementById('notification');

    // Fetch and display users
    const fetchUsers = async () => {
        showLoader(true);
        try {
            const response = await fetch('/users');
            const users = await response.json();
            
            userBody.innerHTML = '';
            if (users.length === 0) {
                emptyState.classList.remove('hidden');
            } else {
                emptyState.classList.add('hidden');
                users.forEach(user => {
                    const tr = document.createElement('tr');
                    tr.innerHTML = `
                        <td>${user.username}</td>
                        <td>••••••••</td>
                        <td>
                            <button class="delete-btn" data-username="${user.username}">
                                Delete
                            </button>
                        </td>
                    `;
                    userBody.appendChild(tr);
                });

                // Add delete event listeners
                document.querySelectorAll('.delete-btn').forEach(btn => {
                    btn.addEventListener('click', () => deleteUser(btn.dataset.username));
                });
            }
        } catch (error) {
            showNotification('Failed to fetch users', 'error');
        } finally {
            showLoader(false);
        }
    };

    // Add user
    userForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        const submitBtn = document.getElementById('submit-btn');
        submitBtn.disabled = true;
        submitBtn.innerText = 'Creating...';

        try {
            const response = await fetch('/add-user', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, password })
            });

            const result = await response.json();
            if (response.ok) {
                showNotification('User added successfully!', 'success');
                userForm.reset();
                fetchUsers();
            } else {
                showNotification(result.detail || 'Failed to add user', 'error');
            }
        } catch (error) {
            showNotification('An error occurred', 'error');
        } finally {
            submitBtn.disabled = false;
            submitBtn.innerText = 'Add User';
        }
    });

    // Delete user
    const deleteUser = async (username) => {
        if (!confirm(`Are you sure you want to delete user "${username}"?`)) return;

        try {
            const response = await fetch(`/delete-user/${username}`, {
                method: 'DELETE'
            });

            if (response.ok) {
                showNotification('User deleted successfully!', 'success');
                fetchUsers();
            } else {
                const result = await response.json();
                showNotification(result.detail || 'Failed to delete user', 'error');
            }
        } catch (error) {
            showNotification('An error occurred', 'error');
        }
    };

    // UI Helpers
    const showLoader = (show) => {
        if (show) {
            loader.classList.remove('hidden');
            userBody.classList.add('hidden');
        } else {
            loader.classList.add('hidden');
            userBody.classList.remove('hidden');
        }
    };

    const showNotification = (message, type) => {
        notification.innerText = message;
        notification.className = `notification show ${type}`;
        setTimeout(() => {
            notification.classList.remove('show');
        }, 3000);
    };

    refreshBtn.addEventListener('click', fetchUsers);

    // Initial load
    fetchUsers();
});
