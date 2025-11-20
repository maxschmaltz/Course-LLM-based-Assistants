/**
 * Client-side MyST Plugin to hide references sections using DOM manipulation
 */

const hideReferencesDirective = {
  name: 'hide_references',
  doc: 'Injects a script to hide the references section on page load',
  run() {
    // Return a raw HTML node that contains a script
    return [
      {
        type: 'html',
        value: `<script>
          (function() {
            // Wait for DOM to be ready
            if (document.readyState === 'loading') {
              document.addEventListener('DOMContentLoaded', hideReferences);
            } else {
              hideReferences();
            }
            
            function hideReferences() {
              // Find and hide the references section
              const referencesSection = document.getElementById('references');
              if (referencesSection) {
                referencesSection.style.display = 'none';
                console.log('References section hidden');
              }
              
              // Alternative: find by class
              const sections = document.querySelectorAll('section.article-grid');
              sections.forEach(section => {
                const header = section.querySelector('header');
                if (header && header.textContent.includes('References')) {
                  section.style.display = 'none';
                  console.log('References section hidden by header text');
                }
              });
            }
          })();
        </script>`,
      },
    ];
  },
};

const plugin = {
  name: 'Hide References Client-Side',
  directives: [hideReferencesDirective],
};

export default plugin;
