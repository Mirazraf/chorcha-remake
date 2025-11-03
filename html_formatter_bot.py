#!/usr/bin/env python3
"""
HTML Question Bank Converter Bot
Converts question bank HTML files to a cleaner format
Usage: python3 bot.py file1.html file2.html file3.html
"""

import sys
import re
from pathlib import Path
from bs4 import BeautifulSoup

def extract_container_content(html_content):
    """Extract the content inside the container div"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the main container div
    container = soup.find('div', class_='container')
    
    if container:
        # Get all the question cards and content
        return str(container)
    return None

def create_modified_html(container_content, title="DU A Unit Admission Question Bank - চর্চা"):
    """Create a new HTML structure with the container content"""
    
    template = f'''<html
  class="inter_a74e9378-module__elCoYG__variable noto_serif_bengali_87c52a22-module__4xfC0q__variable dark bprogress-busy"
  data-scroll-behavior="smooth" lang="en" style="color-scheme: dark;">

<head>
  <link data-precedence="next" href="../../../e42da78b4eb363d8.css" rel="stylesheet" />
  <link data-precedence="next" href="../../../3a4673b8fdafafdb.css" rel="stylesheet" />
  <link as="script" fetchpriority="low" href="../../../51d636fc8762e653.js" rel="preload" />
  <script src="../../../script.js"></script>
  <script async="" src="https://www.googletagmanager.com/gtm.js?id=GTM-5MXSF9XB"></script>
  
  <meta charset="utf-8" />
  <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport" />
  <title>{title}</title>
  
  <link href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css" crossorigin="anonymous"
    integrity="sha384-GvrOXuhMATgEsSwCs4smul74iXGOixntILdUW9XmUC6+HX0sLNAK3q71HotJqlAn" rel="stylesheet" />
  
  <style id="_goober">
    @keyframes go2264125279 {{
      from {{ transform: scale(0) rotate(45deg); opacity: 0; }}
      to {{ transform: scale(1) rotate(45deg); opacity: 1; }}
    }}
    @keyframes go3020080000 {{
      from {{ transform: scale(0); opacity: 0; }}
      to {{ transform: scale(1); opacity: 1; }}
    }}
  </style>

  <style>
    :root {{
      --bprogress-color: #10B981;
      --bprogress-height: 3px;
      --bprogress-spinner-size: 18px;
      --bprogress-z-index: 99999;
    }}
    
    .bprogress {{
      width: 0;
      height: 0;
      pointer-events: none;
      z-index: var(--bprogress-z-index);
    }}
  </style>
</head>

<body cz-shortcut-listen="true">
  <div hidden=""></div>
  <noscript><iframe height="0" src="https://www.googletagmanager.com/ns.html?id=GTM-5MXSF9XB"
      style="display:none;visibility:hidden" width="0"></iframe></noscript>

  <div>
    <aside
      class="hidden lg:fixed lg:inset-y-0 z-30 lg:flex lg:flex-col bg-sidebar dark:bg-sidebar-dark transition-all duration-300 lg:w-72">
      <div class="flex h-20 items-center justify-between px-5">
        <div class="flex items-center">
          <a href="../../../dashboard.html">
            <img alt="Chorcha Logo" class="h-8 w-auto dark:hidden" src="/svgs/logo.png" />
          </a>
          <a href="../../../dashboard.html">
            <img alt="Chorcha Logo" class="h-8 w-auto hidden dark:block" src="../../../logo-dark.png" />
          </a>
        </div>
        <button class="transition-transform">
          <svg class="h-6 w-6 translate-y-[3px] text-gray-400" fill="currentColor" height="1em" 
               stroke="currentColor" stroke-width="0" viewbox="0 0 24 24" width="1em"
               xmlns="http://www.w3.org/2000/svg">
            <path d="M6 21a3 3 0 0 1 -3 -3v-12a3 3 0 0 1 3 -3h12a3 3 0 0 1 3 3v12a3 3 0 0 1 -3 3zm8 -16h-8a1 1 0 0 0 -1 1v12a1 1 0 0 0 1 1h8z"></path>
          </svg>
        </button>
      </div>
      
      <nav class="flex-1 overflow-y-auto px-4 mt-6 space-y-2">
        <div>
          <a class="w-full rounded-xl flex items-center gap-x-4 px-4 py-2 sidebar-tab-inactive"
             href="../../../dashboard.html">
            <svg fill="none" height="18" viewbox="0 0 24 24" width="18" xmlns="http://www.w3.org/2000/svg">
              <path d="M7.99932 21L7.74868 17.4911C7.61394 15.6046 9.10803 14 10.9993 14C12.8906 14 14.3847 15.6046 14.25 17.4911L13.9993 21"
                    stroke="currentColor" stroke-width="1.5"></path>
              <path d="M1.35139 12.2135C0.998371 9.91624 0.821861 8.76763 1.25617 7.74938C1.69047 6.73112 2.65403 6.03443 4.58114 4.64106L6.02099 3.6C8.41829 1.86667 9.61694 1 11 1C12.3831 1 13.5817 1.86667 15.979 3.6L17.4189 4.64106C19.346 6.03443 20.3095 6.73112 20.7438 7.74938C21.1781 8.76763 21.0016 9.91624 20.6486 12.2135L20.3476 14.1724C19.8471 17.4289 19.5969 19.0572 18.429 20.0286C17.2611 21 15.5537 21 12.1388 21H9.86119C6.44633 21 4.73891 21 3.571 20.0286C2.40309 19.0572 2.15287 17.4289 1.65243 14.1724L1.35139 12.2135Z"
                    stroke="currentColor" stroke-linejoin="round" stroke-width="1.5"></path>
            </svg>
            <span class="truncate">ড্যাশবোর্ড</span>
          </a>
        </div>
        <div>
          <a class="w-full rounded-xl flex items-center gap-x-4 px-4 py-2 sidebar-tab-inactive"
             href="../../../question-bank.html">
            <svg fill="none" height="18" viewbox="0 0 24 24" width="18" xmlns="http://www.w3.org/2000/svg">
              <path d="M20.198 3L3.802 3C3.05147 3 2.6762 3 2.41637 3.17726C2.28768 3.26505 2.18133 3.38109 2.10567 3.51627C1.9529 3.78921 1.99024 4.15793 2.06493 4.89537C2.18958 6.12624 2.2519 6.74168 2.57823 7.18168C2.74084 7.40095 2.94701 7.58519 3.18414 7.72315C3.65999 8 4.28635 8 5.53908 8L18.4609 8C19.7136 8 20.34 8 20.8159 7.72315C21.053 7.58519 21.2592 7.40095 21.4218 7.18168C21.7481 6.74168 21.8104 6.12624 21.9351 4.89537C22.0098 4.15793 22.0471 3.78921 21.8943 3.51627C21.8187 3.38109 21.7123 3.26505 21.5836 3.17726C21.3238 3 20.9485 3 20.198 3Z"
                    stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
              <path d="M3 8L3 13.0408C3 16.7928 3 18.6688 4.17157 19.8344C5.34315 21 7.22876 21 11 21H13C16.7712 21 18.6569 21 19.8284 19.8344C21 18.6688 21 16.7928 21 13.0408V8"
                    stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
              <path d="M10 11L14 11" stroke="currentColor" stroke-linecap="round" stroke-width="1.5"></path>
            </svg>
            <span class="truncate">আর্কাইভ</span>
          </a>
        </div>
        <div>
          <a class="w-full rounded-xl flex items-center gap-x-4 px-4 py-2 sidebar-tab-inactive"
             href="../../../profile.html">
            <svg fill="none" height="18" viewbox="0 0 24 24" width="18" xmlns="http://www.w3.org/2000/svg">
              <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.5"></circle>
              <path d="M7.5 17C9.8317 14.5578 14.1432 14.4428 16.5 17M14.4951 9.5C14.4951 10.8807 13.3742 12 11.9915 12C10.6089 12 9.48797 10.8807 9.48797 9.5C9.48797 8.11929 10.6089 7 11.9915 7C13.3742 7 14.4951 8.11929 14.4951 9.5Z"
                    stroke="currentColor" stroke-linecap="round" stroke-width="1.5"></path>
            </svg>
            <span class="truncate">প্রোফাইল</span>
          </a>
        </div>
      </nav>
    </aside>

    <header class="app:hidden lg:hidden fixed top-0 inset-x-0 z-40 flex items-center justify-between px-4 py-2 h-16 shadow-sm bg-sidebar dark:bg-sidebar-dark">
      <button>
        <svg aria-hidden="true" class="h-6 w-6" data-slot="icon" fill="none" stroke="currentColor"
             stroke-width="1.5" viewbox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path d="M3.75 9h16.5m-16.5 6.75h16.5" stroke-linecap="round" stroke-linejoin="round"></path>
        </svg>
      </button>
      <img alt="logo" class="h-8 w-auto dark:hidden" src="/svgs/logo.png" />
      <img alt="logo" class="h-8 w-auto hidden dark:block" src="../../../logo-dark.png" />
    </header>

    <div class="fixed inset-0 z-50 lg:hidden transition-transform duration-300 -translate-x-full pointer-events-none">
      <div class="absolute inset-0 bg-black/40 transition-opacity duration-300 opacity-0"></div>
      <div class="relative w-72 max-w-full h-full shadow-xl bg-sidebar dark:bg-sidebar-dark flex flex-col">
        <div class="flex items-center justify-between px-4 h-16">
          <div class="flex items-center">
            <div>
              <a href="/"><img alt="Chorcha Logo" class="h-8 w-auto dark:hidden" src="/svgs/logo.png" /></a>
              <a href="/"><img alt="Chorcha Logo" class="h-8 w-auto hidden dark:block" src="../../../logo-dark.png" /></a>
            </div>
          </div>
          <button>
            <svg class="h-6 w-6" fill="none" height="1em" stroke="currentColor" stroke-linecap="round"
                 stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="1em"
                 xmlns="http://www.w3.org/2000/svg">
              <path d="M18 6l-12 12"></path>
              <path d="M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        <nav class="flex-1 overflow-y-auto px-2 space-y-2 mt-5">
          <div>
            <a class="w-full rounded-xl flex items-center gap-x-4 px-4 py-2 sidebar-tab-inactive"
               href="../../../dashboard.html">
              <svg fill="none" height="18" viewbox="0 0 24 24" width="18" xmlns="http://www.w3.org/2000/svg">
                <path d="M7.99932 21L7.74868 17.4911C7.61394 15.6046 9.10803 14 10.9993 14C12.8906 14 14.3847 15.6046 14.25 17.4911L13.9993 21"
                      stroke="currentColor" stroke-width="1.5"></path>
                <path d="M1.35139 12.2135C0.998371 9.91624 0.821861 8.76763 1.25617 7.74938C1.69047 6.73112 2.65403 6.03443 4.58114 4.64106L6.02099 3.6C8.41829 1.86667 9.61694 1 11 1C12.3831 1 13.5817 1.86667 15.979 3.6L17.4189 4.64106C19.346 6.03443 20.3095 6.73112 20.7438 7.74938C21.1781 8.76763 21.0016 9.91624 20.6486 12.2135L20.3476 14.1724C19.8471 17.4289 19.5969 19.0572 18.429 20.0286C17.2611 21 15.5537 21 12.1388 21H9.86119C6.44633 21 4.73891 21 3.571 20.0286C2.40309 19.0572 2.15287 17.4289 1.65243 14.1724L1.35139 12.2135Z"
                      stroke="currentColor" stroke-linejoin="round" stroke-width="1.5"></path>
              </svg>
              <span class="truncate">ড্যাশবোর্ড</span>
            </a>
          </div>
          <div>
            <a class="w-full rounded-xl flex items-center gap-x-4 px-4 py-2 sidebar-tab-inactive"
               href="../../../question-bank.html">
              <svg fill="none" height="18" viewbox="0 0 24 24" width="18" xmlns="http://www.w3.org/2000/svg">
                <path d="M20.198 3L3.802 3C3.05147 3 2.6762 3 2.41637 3.17726C2.28768 3.26505 2.18133 3.38109 2.10567 3.51627C1.9529 3.78921 1.99024 4.15793 2.06493 4.89537C2.18958 6.12624 2.2519 6.74168 2.57823 7.18168C2.74084 7.40095 2.94701 7.58519 3.18414 7.72315C3.65999 8 4.28635 8 5.53908 8L18.4609 8C19.7136 8 20.34 8 20.8159 7.72315C21.053 7.58519 21.2592 7.40095 21.4218 7.18168C21.7481 6.74168 21.8104 6.12624 21.9351 4.89537C22.0098 4.15793 22.0471 3.78921 21.8943 3.51627C21.8187 3.38109 21.7123 3.26505 21.5836 3.17726C21.3238 3 20.9485 3 20.198 3Z"
                      stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
                <path d="M3 8L3 13.0408C3 16.7928 3 18.6688 4.17157 19.8344C5.34315 21 7.22876 21 11 21H13C16.7712 21 18.6569 21 19.8284 19.8344C21 18.6688 21 16.7928 21 13.0408V8"
                      stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
                <path d="M10 11L14 11" stroke="currentColor" stroke-linecap="round" stroke-width="1.5"></path>
              </svg>
              <span class="truncate">আর্কাইভ</span>
            </a>
          </div>
          <div>
            <a class="w-full rounded-xl flex items-center gap-x-4 px-4 py-2 sidebar-tab-inactive"
               href="../../../profile.html">
              <svg fill="none" height="18" viewbox="0 0 24 24" width="18" xmlns="http://www.w3.org/2000/svg">
                <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="1.5"></circle>
                <path d="M7.5 17C9.8317 14.5578 14.1432 14.4428 16.5 17M14.4951 9.5C14.4951 10.8807 13.3742 12 11.9915 12C10.6089 12 9.48797 10.8807 9.48797 9.5C9.48797 8.11929 10.6089 7 11.9915 7C13.3742 7 14.4951 8.11929 14.4951 9.5Z"
                      stroke="currentColor" stroke-linecap="round" stroke-width="1.5"></path>
              </svg>
              <span class="truncate">প্রোফাইল</span>
            </a>
          </div>
        </nav>
      </div>
    </div>

    <main class="wrapper wrapper-expanded">
      {container_content}
    </main>
  </div>

</body>
</html>'''
    
    return template

def process_html_file(input_file):
    """Process a single HTML file"""
    try:
        input_path = Path(input_file)
        
        if not input_path.exists():
            print(f"❌ Error: File '{input_file}' not found!")
            return False
        
        print(f"📄 Processing: {input_file}")
        
        # Read the input file
        with open(input_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Extract container content
        container_content = extract_container_content(html_content)
        
        if not container_content:
            print(f"❌ Error: Could not find container div in '{input_file}'")
            return False
        
        # Extract title from original HTML if present
        soup = BeautifulSoup(html_content, 'html.parser')
        title_tag = soup.find('title')
        title = title_tag.string if title_tag else "DU A Unit Admission Question Bank - চর্চা"
        
        # Create modified HTML
        modified_html = create_modified_html(container_content, title)
        
        # Overwrite the original file
        output_path = input_path
        
        # Write modified HTML
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(modified_html)
        
        print(f"✅ Success: File '{output_path}' has been modified")
        return True
        
    except Exception as e:
        print(f"❌ Error processing '{input_file}': {str(e)}")
        return False

def main():
    """Main function to handle command line arguments"""
    
    print("=" * 60)
    print("🤖 HTML Question Bank Converter Bot")
    print("=" * 60)
    print()
    
    if len(sys.argv) < 2:
        print("Usage: python3 bot.py file1.html file2.html file3.html")
        print()
        print("Example:")
        print("  python3 bot.py question1.html")
        print("  python3 bot.py file1.html file2.html file3.html")
        sys.exit(1)
    
    # Get all HTML files from command line arguments
    input_files = sys.argv[1:]
    
    print(f"📋 Files to process: {len(input_files)}")
    print()
    
    # Process each file
    success_count = 0
    fail_count = 0
    
    for input_file in input_files:
        if process_html_file(input_file):
            success_count += 1
        else:
            fail_count += 1
        print()
    
    # Summary
    print("=" * 60)
    print(f"✅ Successfully processed: {success_count}")
    print(f"❌ Failed: {fail_count}")
    print(f"📊 Total: {len(input_files)}")
    print("=" * 60)

if __name__ == "__main__":
    main()