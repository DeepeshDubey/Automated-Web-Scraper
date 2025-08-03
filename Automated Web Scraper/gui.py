import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from scraper import WebScraper
import threading

class ScraperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraper")
        self.root.geometry("600x500")
        self.scraper = WebScraper()
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('TEntry', font=('Arial', 10))
        self.style.configure('TCombobox', font=('Arial', 10))
        
        self.create_widgets()
    
    def create_widgets(self):
        """Create and arrange all GUI widgets"""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # URL Entry
        ttk.Label(main_frame, text="Website URL:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.url_entry = ttk.Entry(main_frame, width=50)
        self.url_entry.grid(row=0, column=1, sticky=tk.EW, pady=(0, 5), padx=(5, 0))
        self.url_entry.insert(0, "https://example.com")
        
        # Element Type
        ttk.Label(main_frame, text="Element Type:").grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        self.element_type = ttk.Combobox(main_frame, values=['class', 'id', 'tag'], state='readonly')
        self.element_type.grid(row=1, column=1, sticky=tk.EW, pady=(0, 5), padx=(5, 0))
        self.element_type.set('class')
        
        # Element Value
        ttk.Label(main_frame, text="Element Value:").grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        self.element_value = ttk.Entry(main_frame, width=50)
        self.element_value.grid(row=2, column=1, sticky=tk.EW, pady=(0, 5), padx=(5, 0))
        self.element_value.insert(0, "example-class")
        
        # Buttons Frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=(10, 5))
        
        self.scrape_button = ttk.Button(button_frame, text="Scrape Website", command=self.start_scraping)
        self.scrape_button.pack(side=tk.LEFT, padx=(0, 5))
        
        self.export_csv_button = ttk.Button(button_frame, text="Export to CSV", command=lambda: self.export_data('csv'))
        self.export_csv_button.pack(side=tk.LEFT, padx=(0, 5))
        self.export_csv_button.config(state=tk.DISABLED)
        
        self.export_excel_button = ttk.Button(button_frame, text="Export to Excel", command=lambda: self.export_data('excel'))
        self.export_excel_button.pack(side=tk.LEFT)
        self.export_excel_button.config(state=tk.DISABLED)
        
        # Results Frame
        results_frame = ttk.LabelFrame(main_frame, text="Scraped Results", padding="5")
        results_frame.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW, pady=(10, 0))
        
        # Configure grid weights for resizing
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        # Results Treeview
        self.tree = ttk.Treeview(results_frame, columns=('text', 'element', 'tag'), show='headings')
        self.tree.heading('text', text='Text Content')
        self.tree.heading('element', text='Element')
        self.tree.heading('tag', text='Tag Name')
        
        # Add scrollbars
        y_scroll = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.tree.yview)
        x_scroll = ttk.Scrollbar(results_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)
        
        # Grid layout for tree and scrollbars
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)
        y_scroll.grid(row=0, column=1, sticky=tk.NS)
        x_scroll.grid(row=1, column=0, sticky=tk.EW)
        
        # Configure treeview resizing
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=5, column=0, columnspan=2, sticky=tk.EW, pady=(10, 0))
        
        # Store scraped data
        self.scraped_data = None
    
    def start_scraping(self):
        """Start scraping in a separate thread to keep GUI responsive"""
        url = self.url_entry.get().strip()
        element_type = self.element_type.get()
        element_value = self.element_value.get().strip()
        
        if not url or not element_value:
            messagebox.showerror("Error", "Please enter both URL and element value")
            return
        
        # Disable buttons during scraping
        self.scrape_button.config(state=tk.DISABLED)
        self.export_csv_button.config(state=tk.DISABLED)
        self.export_excel_button.config(state=tk.DISABLED)
        self.status_var.set("Scraping in progress...")
        
        # Start scraping in a separate thread
        threading.Thread(
            target=self.scrape_website,
            args=(url, element_type, element_value),
            daemon=True
        ).start()
    
    def scrape_website(self, url, element_type, element_value):
        """Perform the actual scraping"""
        try:
            data = self.scraper.scrape(url, element_type, element_value)
            self.scraped_data = data
            
            # Update GUI with results
            self.root.after(0, self.display_results, data)
            self.root.after(0, self.update_status, f"Found {len(data)} items. Ready")
            
        except Exception as e:
            self.root.after(0, messagebox.showerror, "Error", str(e))
            self.root.after(0, self.update_status, "Error occurred")
        
        finally:
            # Re-enable buttons
            self.root.after(0, self.scrape_button.config, {'state': tk.NORMAL})
            if self.scraped_data:
                self.root.after(0, self.export_csv_button.config, {'state': tk.NORMAL})
                self.root.after(0, self.export_excel_button.config, {'state': tk.NORMAL})
    
    def display_results(self, data):
        """Display scraped data in the treeview"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add new items
        for item in data:
            self.tree.insert('', tk.END, values=(
                item['text'][:100] + '...' if len(item['text']) > 100 else item['text'],
                f"{item['element_type']}:{item['element_value']}",
                item['tag_name']
            ))
    
    def export_data(self, format_type):
        """Export data to CSV or Excel"""
        if not self.scraped_data:
            messagebox.showerror("Error", "No data to export")
            return
        
        try:
            if format_type == 'csv':
                filetypes = [('CSV files', '*.csv')]
                default_ext = '.csv'
                save_func = self.scraper.save_to_csv
            else:
                filetypes = [('Excel files', '*.xlsx')]
                default_ext = '.xlsx'
                save_func = self.scraper.save_to_excel
            
            filename = filedialog.asksaveasfilename(
                defaultextension=default_ext,
                filetypes=filetypes,
                title="Save scraped data"
            )
            
            if filename:
                saved_file = save_func(self.scraped_data, filename)
                messagebox.showinfo("Success", f"Data successfully saved to {saved_file}")
                self.status_var.set(f"Data exported to {saved_file}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export data: {e}")
            self.status_var.set("Export failed")
    
    def update_status(self, message):
        """Update the status bar message"""
        self.status_var.set(message)

def main():
    root = tk.Tk()
    app = ScraperGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()