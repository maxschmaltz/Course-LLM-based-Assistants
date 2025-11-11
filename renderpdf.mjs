const pdfDirective = {
  name: 'pdf',
  doc: 'A directive for embedding PDF files from a URL into your document.',
  alias: ['pdf-viewer', 'pdf-embed'],
  arg: {
    type: String,
    required: true,
    doc: 'The URL of the PDF file to embed',
  },
  options: {
    width: {
      type: String,
      doc: 'Width of the PDF viewer. Default is `100%`.',
    },
    height: {
      type: String,
      doc: 'Height of the PDF viewer. Default is `600px`.',
    },
    viewer: {
      type: String,
      doc: 'PDF viewer to use: "google", "mozilla", or "native". Default is "google".',
    },
  },
  run(data) {
    const url = data.arg;
    const width = data.options?.width ?? '100%';
    const height = data.options?.height ?? '600px';
    const viewer = data.options?.viewer ?? 'google';
    
    let embedUrl = url;
    
    // Use proxy viewer for better compatibility
    if (viewer === 'google') {
      embedUrl = `https://docs.google.com/viewer?url=${encodeURIComponent(url)}&embedded=true`;
    } else if (viewer === 'mozilla') {
      embedUrl = `https://mozilla.github.io/pdf.js/web/viewer.html?file=${encodeURIComponent(url)}`;
    }
    // else use native iframe with direct URL
    
    return [
      {
        type: 'html',
        value: `<iframe src="${embedUrl}" width="${width}" height="${height}" style="border: 1px solid #ccc;" allowfullscreen></iframe>`
      }
    ];
  },
};

const plugin = {
  name: 'PDF Embed Plugin',
  description: 'Embed PDF files from URLs directly into your MyST documents',
  directives: [pdfDirective],
};

export default plugin;