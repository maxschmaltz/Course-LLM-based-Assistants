const pdfDirective = {
  name: 'renderpdf',
  doc: 'A directive for embedding PDF files from a URL into your document.',
  alias: ['pdf-viewer', 'pdf-embed'],
  arg: {
    type: String,
    required: true,
    doc: 'The URL of the PDF file to embed, e.g. https://example.com/document.pdf',
  },
  options: {
    width: {
      type: String,
      doc: 'Width of the PDF viewer, for example, `100%`, `800px`, or `50%`. Default is `100%`.',
    },
    height: {
      type: String,
      doc: 'Height of the PDF viewer, for example, `600px`, `80vh`. Default is `600px`.',
    },
    page: {
      type: Number,
      doc: 'Specific page number to display (if supported by viewer). Default shows all pages.',
    },
    toolbar: {
      type: Boolean,
      doc: 'Whether to show PDF toolbar controls. Default is true.',
    },
  },
  body: {
    type: String,
    doc: 'Optional caption for the PDF embed.',
  },
  run(data) {
    const url = data.arg;
    
    // Validate URL
    if (!url || (!url.startsWith('http://') && !url.startsWith('https://'))) {
      return [
        {
          type: 'admonition',
          kind: 'danger',
          children: [
            {
              type: 'paragraph',
              children: [
                {
                  type: 'text',
                  value: 'Invalid PDF URL. Please provide a valid http:// or https:// URL.',
                },
              ],
            },
          ],
        },
      ];
    }

    // Parse options
    const width = data.options?.width ?? '100%';
    const height = data.options?.height ?? '600px';
    const toolbar = data.options?.toolbar !== false ? 1 : 0;
    
    // Construct PDF URL with parameters
    let pdfUrl = url;
    if (data.options?.page) {
      pdfUrl += `#page=${data.options.page}`;
    }
    if (!toolbar) {
      pdfUrl += `#toolbar=${toolbar}`;
    }

    // Create iframe node
    const iframe = {
      type: 'iframe',
      src: pdfUrl,
      width,
      height,
    };

    // If there's a caption, wrap in a container
    if (data.body) {
      return [
        {
          type: 'container',
          children: [
            iframe,
            {
              type: 'caption',
              children: [
                {
                  type: 'paragraph',
                  children: [{ type: 'text', value: data.body }],
                },
              ],
            },
          ],
        },
      ];
    }

    return [iframe];
  },
};

const plugin = {
  name: 'PDF Embed Plugin',
  description: 'Embed PDF files from URLs directly into your MyST documents',
  directives: [pdfDirective],
};

export default plugin;