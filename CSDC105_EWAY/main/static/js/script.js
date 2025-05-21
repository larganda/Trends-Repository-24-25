function toggleDropdown() {
      const menu = document.getElementById("dropdown-menu");
      menu.style.display = (menu.style.display === "flex") ? "none" : "flex";
    }

    // Close dropdown if clicked outside
    window.addEventListener("click", function (e) {
      const dropdown = document.getElementById("dropdown-menu");
      const profile = document.querySelector(".user-profile");
        if (!profile.contains(e.target)) {
          dropdown.style.display = "none";
        }
      });

    function searchUserDetails() {
      const searchTerm = document.getElementById('searchInput').value.toLowerCase();
      const resultsContainer = document.getElementById('userDetails');
      const noResults = document.getElementById('noResults');
      
      // Clear previous results
      resultsContainer.innerHTML = '';
      resultsContainer.style.display = 'none';
      noResults.style.display = 'none';

      if (!searchTerm) {
        return; // Don't search if empty
      }

      // In a real implementation, you would make an API call here
      // For now, we'll just show no results
      noResults.style.display = 'block';
    }

    // Modal functionality
    function openModal(imageSrc) {
      const modal = document.getElementById('imageModal');
      const modalImg = document.getElementById('modalImage');
      modal.style.display = 'block';
      modalImg.src = imageSrc;
    }

    function closeModal() {
      const modal = document.getElementById('imageModal');
      modal.style.display = 'none';
    } 

    // Close modal when clicking outside
    window.onclick = function (event) {
      const modal = document.getElementById('imageModal');
      if (event.target === modal) {
      modal.style.display = 'none';
    }
    }

    // Close modal with ESC key
    document.onkeydown = function(evt) {
      evt = evt || window.event;
      if (evt.key === "Escape") {
        closeModal();
      }
    };

    // Scroll to top button
    const scrollTopBtn = document.getElementById('scrollTop');
    
    window.addEventListener('scroll', () => {
      if (window.pageYOffset > 300) {
        scrollTopBtn.classList.add('active');
      } else {
        scrollTopBtn.classList.remove('active');
      }
    });
    
    scrollTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });

  document.getElementById('signInForm').addEventListener('submit', function(e) {
  const email = document.getElementById('email').value;
  const emailError = document.getElementById('emailError');

  if (!email.includes('@')) {
    e.preventDefault();
    emailError.classList.remove('hidden');
    return;
  }
  emailError.classList.add('hidden');

  // Show loading but do NOT prevent form submit
  const submitBtn = e.target.querySelector('button[type="submit"]');
  submitBtn.innerHTML = 'Signing In...';
});
