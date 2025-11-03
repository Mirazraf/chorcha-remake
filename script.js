// DU A Unit Admission Question Bank - Interactive Features
(function() {
    'use strict';

    // State management
    let isAnswersVisible = false;
    let answeredQuestions = new Set();

    // Initialize on page load
    document.addEventListener('DOMContentLoaded', function() {
        initializeSidebar();
        initializeQuestions();
        initializeEyeButton();
    });

    // Sidebar functionality
    function initializeSidebar() {
        const sidebarTogglers = document.querySelectorAll('button');
        const sidebar = document.querySelector('aside');
        const mobileSidebar = document.querySelector('.fixed.inset-0.z-50.lg\\:hidden');
        const overlay = mobileSidebar ? mobileSidebar.querySelector('.absolute.inset-0.bg-black\\/40') : null;
        const closeButton = mobileSidebar ? mobileSidebar.querySelector('button svg.h-6.w-6') : null;

        // Find the correct toggle buttons
        let mobileMenuButton = null;
        let desktopToggleButton = null;

        sidebarTogglers.forEach(button => {
            const svg = button.querySelector('svg');
            if (svg) {
                // Mobile menu button (hamburger)
                if (svg.getAttribute('viewBox') === '0 0 24 24' && svg.querySelector('path[d*="M3.75 9h16.5"]')) {
                    mobileMenuButton = button;
                }
                // Desktop sidebar toggle button
                if (svg.classList.contains('translate-y-\\[3px\\]')) {
                    desktopToggleButton = button;
                }
            }
        });

        // Mobile sidebar toggle
        if (mobileMenuButton && mobileSidebar) {
            mobileMenuButton.addEventListener('click', function() {
                mobileSidebar.classList.remove('-translate-x-full', 'pointer-events-none');
                if (overlay) {
                    overlay.classList.remove('opacity-0');
                }
            });
        }

        // Close mobile sidebar
        if (closeButton && mobileSidebar) {
            closeButton.closest('button').addEventListener('click', closeMobileSidebar);
        }

        if (overlay && mobileSidebar) {
            overlay.addEventListener('click', closeMobileSidebar);
        }

        function closeMobileSidebar() {
            mobileSidebar.classList.add('-translate-x-full', 'pointer-events-none');
            if (overlay) {
                overlay.classList.add('opacity-0');
            }
        }

        // Desktop sidebar toggle
        if (desktopToggleButton && sidebar) {
            desktopToggleButton.addEventListener('click', function() {
                sidebar.classList.toggle('lg:w-72');
                sidebar.classList.toggle('lg:w-20');
                
                const main = document.querySelector('main');
                if (main) {
                    main.classList.toggle('wrapper-expanded');
                    main.classList.toggle('wrapper-collapsed');
                }

                // Toggle text visibility
                const sidebarTexts = sidebar.querySelectorAll('.truncate');
                sidebarTexts.forEach(text => {
                    text.style.display = text.style.display === 'none' ? '' : 'none';
                });
            });
        }
    }

    // Initialize questions functionality
    function initializeQuestions() {
        const questionCards = document.querySelectorAll('.rounded-xl.p-4.flex.flex-col.space-y-2');

        questionCards.forEach((card, index) => {
            const options = card.querySelectorAll('.grid.md\\:grid-cols-2 > div');
            const explanation = card.querySelector('.card-bekkha');
            
            // Hide explanation by default
            if (explanation) {
                explanation.style.display = 'none';
            }

            // Store which option has the correct class and normalize ALL options
            let correctOptionIndex = -1;
            options.forEach((option, idx) => {
                const optionContainer = option.querySelector('button > div');
                const indicator = option.querySelector('div > div');
                
                if (indicator) {
                    // Check if this indicator has the 'correct' class
                    if (indicator.classList.contains('correct')) {
                        correctOptionIndex = idx;
                        // Keep the class for reference but normalize styling
                        indicator.classList.add('original-correct');
                    }
                    
                    // FORCE all options to have the same appearance - remove ALL backgrounds
                    indicator.style.setProperty('background-color', 'transparent', 'important');
                    indicator.style.borderColor = 'rgb(107, 114, 128)'; // gray-500
                    indicator.style.borderWidth = '1.5px';
                    indicator.style.borderStyle = 'solid';
                    indicator.style.color = '';
                }
                
                // Also remove background from the parent container
                if (optionContainer) {
                    optionContainer.style.setProperty('background-color', '', 'important');
                }
            });
            
            // Store the correct answer index
            card.dataset.correctIndex = correctOptionIndex;

            // Add click handlers to options
            options.forEach((optionDiv, optionIndex) => {
                const button = optionDiv.querySelector('button');
                if (button) {
                    button.addEventListener('click', function() {
                        if (!answeredQuestions.has(index)) {
                            handleAnswerClick(card, optionDiv, optionIndex, index);
                        }
                    });
                }
            });
        });
    }

    // Handle answer click
    function handleAnswerClick(card, selectedOption, selectedIndex, questionIndex) {
        const options = card.querySelectorAll('.grid.md\\:grid-cols-2 > div');
        const explanation = card.querySelector('.card-bekkha');
        const correctIndex = parseInt(card.dataset.correctIndex);
        
        // Check if the selected answer is correct
        const isCorrect = selectedIndex === correctIndex;

        // Mark the question as answered
        answeredQuestions.add(questionIndex);

        // Style the selected option
        const selectedIndicator = selectedOption.querySelector('div > div');
        if (isCorrect) {
            // Correct answer - mark green with !important to override CSS
            selectedIndicator.style.setProperty('background-color', '#22c55e', 'important');
            selectedIndicator.style.setProperty('border-color', '#22c55e', 'important');
            selectedIndicator.style.setProperty('color', 'white', 'important');
        } else {
            // Wrong answer - mark selected as red with !important
            selectedIndicator.style.setProperty('background-color', '#ef4444', 'important');
            selectedIndicator.style.setProperty('border-color', '#ef4444', 'important');
            selectedIndicator.style.setProperty('color', 'white', 'important');
            
            // Also show correct answer in green with !important
            if (correctIndex >= 0 && correctIndex < options.length) {
                const correctOption = options[correctIndex];
                const correctIndicator = correctOption.querySelector('div > div');
                correctIndicator.style.setProperty('background-color', '#22c55e', 'important');
                correctIndicator.style.setProperty('border-color', '#22c55e', 'important');
                correctIndicator.style.setProperty('color', 'white', 'important');
            }
        }

        // Show explanation
        if (explanation) {
            explanation.style.display = 'block';
        }

        // Disable all options for this question
        options.forEach(option => {
            const button = option.querySelector('button');
            if (button) {
                button.style.pointerEvents = 'none';
            }
        });
    }

    // Initialize eye button functionality
    function initializeEyeButton() {
        const eyeButton = document.querySelector('button[data-event="eye_icon_review"]');
        
        if (eyeButton) {
            eyeButton.addEventListener('click', function() {
                isAnswersVisible = !isAnswersVisible;
                toggleAnswersVisibility();
                
                // Update eye icon
                const eyeIcon = eyeButton.querySelector('svg');
                if (eyeIcon && !isAnswersVisible) {
                    // You can change icon here if needed
                    eyeButton.style.opacity = '0.7';
                } else if (eyeIcon) {
                    eyeButton.style.opacity = '1';
                }
            });
        }
    }

    // Toggle answers visibility
    function toggleAnswersVisibility() {
        const questionCards = document.querySelectorAll('.rounded-xl.p-4.flex.flex-col.space-y-2');

        questionCards.forEach((card, index) => {
            // Skip questions that have been answered
            if (answeredQuestions.has(index)) {
                return;
            }

            const options = card.querySelectorAll('.grid.md\\:grid-cols-2 > div');
            const explanation = card.querySelector('.card-bekkha');
            const correctIndex = parseInt(card.dataset.correctIndex);

            if (isAnswersVisible) {
                // Show correct answer in green with !important
                if (correctIndex >= 0 && correctIndex < options.length) {
                    const correctOption = options[correctIndex];
                    const correctIndicator = correctOption.querySelector('div > div');
                    correctIndicator.style.setProperty('background-color', '#22c55e', 'important');
                    correctIndicator.style.setProperty('border-color', '#22c55e', 'important');
                    correctIndicator.style.setProperty('color', 'white', 'important');
                }

                // Show explanation
                if (explanation) {
                    explanation.style.display = 'block';
                }
            } else {
                // Hide correct answers - reset to transparent background
                options.forEach(option => {
                    const indicator = option.querySelector('div > div');
                    indicator.style.setProperty('background-color', 'transparent', 'important');
                    indicator.style.borderColor = 'rgb(107, 114, 128)'; // gray-500
                    indicator.style.borderWidth = '1.5px';
                    indicator.style.borderStyle = 'solid';
                    indicator.style.removeProperty('color');
                });

                // Hide explanation
                if (explanation) {
                    explanation.style.display = 'none';
                }
            }
        });
    }

    // Add CSS for wrapper classes
    const style = document.createElement('style');
    style.textContent = `
        .wrapper {
            transition: margin-left 0.3s ease;
        }
        .wrapper-expanded {
            margin-left: 0;
        }
        @media (min-width: 1024px) {
            .wrapper-expanded {
                margin-left: 18rem;
            }
            .wrapper-collapsed {
                margin-left: 5rem;
            }
        }
        
        /* Force all option indicators to have transparent background by default */
        .rounded-full.border.shrink-0.flex-center,
        .rounded-full.aspect-square {
            background-color: transparent !important;
            border: 1.5px solid rgb(107, 114, 128) !important;
        }
        
        /* Remove any green background from option containers */
        .bg-gray-100,
        .dark\\:bg-gray-700 {
            background-color: rgb(243 244 246) !important;
        }
        
        .dark .dark\\:bg-gray-700 {
            background-color: rgb(31 31 31) !important;
        }
    `;
    document.head.appendChild(style);
})();