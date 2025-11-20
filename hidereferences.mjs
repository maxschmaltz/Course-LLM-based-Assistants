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
        value: `<!-- Hide References Script Loaded -->
        <script>
          console.log('Hide references script is running!');
          (function() {
            if (document.readyState === 'loading') {
              document.addEventListener('DOMContentLoaded', hideReferences);
            } else {
              hideReferences();
            }
            
            function hideReferences() {
              const referencesSection = document.getElementById('references');
              if (referencesSection) {
                referencesSection.style.display = 'none';
                console.log('✅ References section hidden by ID');
              } else {
                console.log('❌ No element with id="references" found');
              }
              
              const sections = document.querySelectorAll('section.article-grid');
              console.log('Found ' + sections.length + ' article-grid sections');
              
              sections.forEach(section => {
                const header = section.querySelector('header');
                if (header && header.textContent.includes('References')) {
                  section.style.display = 'none';
                  console.log('✅ References section hidden by header text');
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
  description: 'A MyST plugin to hide references sections using client-side JavaScript',
  directives: [hideReferencesDirective],
};

export default plugin;
