// preview.js

// Set up variables
var canvas = document.getElementById('pdf-canvas');
var context = canvas.getContext('2d');
var scale = 1.5;
var currentPage = 1;
var numPages = 0;

// Load the PDF document
PDFJS.getDocument('{{ file.file.url }}').then(function(pdf) {
  numPages = pdf.numPages;

  // Render the first page
  renderPage(currentPage);

  // Add event listeners for the navigation buttons
  document.getElementById('prev-page').addEventListener('click', function() {
    if (currentPage > 1) {
      currentPage--;
      renderPage(currentPage);
    }
  });

  document.getElementById('next-page').addEventListener('click', function() {
    if (currentPage < numPages) {
      currentPage++;
      renderPage(currentPage);
    }
  });
});

// Function to render a specific page
function renderPage(pageNum) {
  PDFJS.getDocument('{{ file.file.url }}').then(function(pdf) {
    pdf.GetPage(pageNum).then(function(page) {
      var viewport = page.getViewport(scale);
      canvas.height = viewport.height;
      canvas.width = viewport.width;

      var renderContext = {
        canvasContext: context,
        viewport: viewport
      };
      page.render(renderContext);
    });
  });
}
renderPage();