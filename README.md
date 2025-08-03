<h1 align="center">Automated Web Scraper with GUI</h1>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.7%2B-blue" alt="Python version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
</p>


<h2>📋 Overview</h2>
<p>A user-friendly GUI application for web scraping built with Python. Extract data from websites by specifying URLs and HTML elements, then export the results to CSV or Excel.</p>

<h2>✨ Features</h2>
<ul>
  <li><strong>Easy-to-use GUI</strong> built with Tkinter</li>
  <li><strong>Flexible scraping</strong> by class, id, or HTML tag</li>
  <li><strong>Export options</strong> to CSV or Excel format</li>
  <li><strong>Threaded scraping</strong> to keep GUI responsive</li>
  <li><strong>Preview results</strong> before exporting</li>
  <li><strong>Error handling</strong> for invalid inputs</li>
</ul>

<h2>🖥️ Usage</h2>
<ol>
  <li>Run the application:
    <pre><code>python gui.py</code></pre>
  </li>
  <li>Enter the target URL and element details:
    <ul>
      <li>Website URL (e.g., <code>https://example.com</code>)</li>
      <li>Element type (class/id/tag)</li>
      <li>Element value (e.g., <code>h1</code> for tag or <code>header</code> for class)</li>
    </ul>
  </li>
  <li>Click "Scrape Website" to extract data</li>
  <li>Export results using the "Export to CSV" or "Export to Excel" buttons</li>
</ol>

<h2>📂 Project Structure</h2>
<pre>
web-scraper-gui/
│
├── scraper.py         # Core scraping functionality
├── gui.py             # Tkinter GUI interface
├── requirements.txt   # Dependencies
├── README.md          # Project documentation
└── output/            # Default export directory (created after first run)
</pre>

<h2>🌐 Examples</h2>
<h3>Scraping Headings from GeeksforGeeks</h3>
<ul>
  <li>URL: <code>https://www.geeksforgeeks.org/computer-networks-network-topology/</code></li>
  <li>Element Type: <code>tag</code></li>
  <li>Element Value: <code>h2</code></li>
</ul>

<h3>Scraping Quotes from Quotes to Scrape</h3>
<ul>
  <li>URL: <code>http://quotes.toscrape.com</code></li>
  <li>Element Type: <code>class</code></li>
  <li>Element Value: <code>quote</code></li>
</ul>

<h2>📦 Dependencies</h2>
<ul>
  <li>Python 3.7+</li>
  <li>requests</li>
  <li>beautifulsoup4</li>
  <li>pandas</li>
  <li>tkinter</li>
</ul>

<h2>🤝 Contributing</h2>
<p>Contributions are welcome! Please follow these steps:</p>
<ol>
  <li>Fork the project</li>
  <li>Create your feature branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
  <li>Commit your changes (<code>git commit -m 'Add some amazing feature'</code>)</li>
  <li>Push to the branch (<code>git push origin feature/AmazingFeature</code>)</li>
  <li>Open a Pull Request</li>
</ol>


<h2>📝 Changelog</h2>
<h3>v1.0.0 (Current)</h3>
<ul>
  <li>Initial release</li>
  <li>Basic scraping functionality</li>
  <li>CSV/Excel export support</li>
</ul>

<h2>❓ FAQ</h2>
<h3>Q: Why am I getting empty results?</h3>
<p>A: This could happen if:
<ol>
  <li>The website requires JavaScript to load content</li>
  <li>The element selector is incorrect</li>
  <li>The website blocks scraping attempts</li>
</ol>
Try different selectors or check the website's robots.txt file.</p>

<h3>Q: Can I scrape multiple pages?</h3>
<p>A: The current version scrapes only the specified page. Pagination support is planned for future releases.</p>
