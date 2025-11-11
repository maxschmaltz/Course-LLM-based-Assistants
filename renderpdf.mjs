const pdfDirective = {
  name: 'renderpdf',
  doc: 'A directive for embedding PDF files with PDF.js',
  arg: {
    type: String,
    required: true,
    doc: 'The URL of the PDF file to embed',
  },
  options: {
    width: { type: String, doc: 'Width. Default: 100%' },
    height: { type: String, doc: 'Height. Default: 600px' },
    page: { type: Number, doc: 'Initial page to display. Default: 1' },
    scale: { type: Number, doc: 'Zoom scale. Default: 1.5' },
  },
  run(data) {
    const url = data.arg;
    const width = data.options?.width ?? '100%';
    const height = data.options?.height ?? '600px';
    const initialPage = data.options?.page ?? 1;
    const scale = data.options?.scale ?? 1.5;
    
    // Generate unique ID for this PDF viewer
    const id = `pdf-viewer-${Math.random().toString(36).substr(2, 9)}`;
    
    const html = `
      <div style="width: ${width}; height: ${height}; border: 1px solid #ccc; overflow: auto; background: #525252;">
        <div id="${id}" style="padding: 20px;">
          <div style="text-align: center; color: white; padding: 20px;">
            Loading PDF...
          </div>
        </div>
      </div>
      
      <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>
      <script>
        (function() {
          // Set worker source
          pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
          
          const container = document.getElementById('${id}');
          const url = '${url}';
          
          // Load the PDF
          pdfjsLib.getDocument(url).promise.then(function(pdf) {
            container.innerHTML = '';
            
            // Render all pages
            for (let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {
              pdf.getPage(pageNum).then(function(page) {
                const viewport = page.getViewport({ scale: ${scale} });
                
                // Create canvas
                const canvas = document.createElement('canvas');
                const context = canvas.getContext('2d');
                canvas.height = viewport.height;
                canvas.width = viewport.width;
                canvas.style.display = 'block';
                canvas.style.margin = '10px auto';
                canvas.style.boxShadow = '0 2px 8px rgba(0,0,0,0.3)';
                
                container.appendChild(canvas);
                
                // Render page
                const renderContext = {
                  canvasContext: context,
                  viewport: viewport
                };
                page.render(renderContext);
              });
            }
          }).catch(function(error) {
            container.innerHTML = '<div style="color: red; padding: 20px;">Error loading PDF: ' + error.message + '</div>';
          });
        })();
      </script>
    `;
    
    return [{ type: 'html', value: html }];
  },
};


const plugin = {
  name: 'PDF Embed Plugin',
  description: 'Embed PDF files from URLs directly into your MyST documents',
  directives: [pdfDirective],
};

export default plugin;