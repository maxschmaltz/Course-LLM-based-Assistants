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
    const showToolbar = data.options?.toolbar !== false;

    // Construct PDF URL with parameters (use a single fragment)
    let pdfUrl = url;
    const fragmentParts = [];
    if (data.options?.page) {
      fragmentParts.push(`page=${data.options.page}`);
    }
    if (!showToolbar) {
      fragmentParts.push(`toolbar=0`);
    }
    if (fragmentParts.length) {
      pdfUrl += `#${fragmentParts.join('&')}`;
    }

    // Create <object> HTML node
    const objectNode = {
      type: 'html',
      value: `<object data="${pdfUrl}" type="application/pdf" width="${width}" height="${height}">` +
             `\n  <p>Your browser does not support embedded PDFs. You can <a href="${url}">download the PDF</a>.</p>\n` +
             `</object>`,
    };

    // If there's a caption, wrap in a container
    if (data.body) {
      return [
        {
          type: 'container',
          children: [
            objectNode,
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

    return [objectNode];
  },
};

const plugin = {
  name: 'PDF Embed Plugin',
  description: 'Embed PDF files from URLs directly into your MyST documents',
  directives: [pdfDirective],
};

export default plugin;