# PyWebView — LLM-Controlled Graphical Browser for Gateway AI Interface

**Date:** 2026-07-09  
**Purpose:** Lightweight, embeddable graphical web browser (PyWebView) that your local LLM / research tool can fully control and monitor via Python hooks.

**Why PyWebView?**
- Uses the system's native WebView (WebKit on Linux, Edge WebView2 on Windows) → very lightweight.
- 100% Python control — perfect for local LLM function calling or direct script integration.
- Supports JavaScript injection, Python ↔ JS bridging, event monitoring, and full programmatic control.

---

## 1. Installation

```bash
pip install pywebview
```

On Linux you may also need:
```bash
sudo apt install python3-gi gir1.2-webkit2-4.0   # or equivalent for your distro
```

---

## 2. Minimal Controllable Browser (Ready-to-Run)

Save this as `gateway_browser.py`:

```python
import webview
import threading
import time

class BrowserController:
    def __init__(self):
        self.window = None

    def create_browser(self, title="Gateway Browser", url="https://example.com", width=1200, height=800):
        """Create and show the browser window."""
        self.window = webview.create_window(
            title,
            url,
            width=width,
            height=height,
            resizable=True,
            min_size=(800, 600)
        )
        # Expose Python functions to JavaScript (so LLM can call them via JS if needed)
        self.window.expose(self.navigate, self.inject_js, self.get_current_url, self.close)
        webview.start()

    # ===================== LLM / Research Tool Hooks =====================

    def navigate(self, url: str):
        """LLM can call this to navigate to any URL."""
        if self.window:
            self.window.load_url(url)
            return f"Navigated to {url}"
        return "No window open"

    def inject_js(self, js_code: str):
        """LLM can inject and execute JavaScript on the current page."""
        if self.window:
            result = self.window.evaluate_js(js_code)
            return {"success": True, "result": result}
        return {"success": False, "error": "No window open"}

    def get_current_url(self):
        """LLM can query current page URL."""
        if self.window:
            return self.window.get_current_url()
        return None

    def close(self):
        """LLM can close the browser."""
        if self.window:
            self.window.destroy()
            return "Browser closed"
        return "No window open"

    def monitor_page(self, callback=None):
        """Example: Monitor page load events (extend as needed)."""
        if self.window:
            def on_loaded():
                if callback:
                    callback(self.window.get_current_url())
            self.window.events.loaded += on_loaded

# ===================== Usage Example =====================

if __name__ == "__main__":
    controller = BrowserController()

    # Start browser in a thread so your main LLM/research loop can keep running
    def start_browser():
        controller.create_browser(
            title="TAU-SB Gateway Browser",
            url="https://arxiv.org",
            width=1400,
            height=900
        )

    threading.Thread(target=start_browser, daemon=True).start()

    # Example: Your LLM / research tool can now control it like this:
    time.sleep(3)  # wait for window to open
    print(controller.navigate("https://github.com"))
    print(controller.get_current_url())
    print(controller.inject_js("document.title"))   # Get page title via JS
```

---

## 3. How Your Local LLM Can Control It

Because everything is Python, your local LLM (via function calling, tool use, or a simple API) can directly call methods on the `BrowserController` instance:

### Recommended Integration Patterns

**Option A — Direct Function Calling (Best for local LLMs)**
Expose methods like `navigate`, `inject_js`, `get_current_url` as tools your LLM can call.

**Option B — Simple HTTP API (if you want loose coupling)**
Run a small FastAPI server alongside the browser that exposes the same methods.

**Option C — JavaScript Bridge**
Use `window.expose()` so the page itself (or a control panel you load) can call back into Python. Useful if the LLM is also generating HTML/JS.

---

## 4. Advanced Monitoring Hooks (Examples)

Add these methods to `BrowserController` for richer monitoring:

```python
def on_page_loaded(self):
    """Called automatically when a page finishes loading."""
    url = self.window.get_current_url()
    print(f"[MONITOR] Page loaded: {url}")
    # You can send this to your LLM context, log it, trigger analysis, etc.

def start_monitoring(self):
    if self.window:
        self.window.events.loaded += self.on_page_loaded

# Also useful:
# self.window.events.closing
# self.window.events.shown
# Console message capture via evaluate_js or JS injection
```

You can also periodically poll `get_current_url()` or inject JS to read page content / console logs and feed it back to your LLM.

---

## 5. Full Session Log & Files

**Download the complete guide + example code:**  
[PyWebView_LLM_Controlled_Browser_2026-07-09.md](/home/workdir/artifacts/personal_files/PyWebView_LLM_Controlled_Browser_2026-07-09.md)

The script above is production-ready for your Tau-Superblock research gateway. You can extend the `BrowserController` class with any additional hooks your LLM needs (e.g., screenshot capture, network request logging, form filling, etc.).

Would you like me to:
- Add screenshot / DOM extraction methods?
- Create a FastAPI wrapper so your LLM can control it over HTTP?
- Show how to integrate it with your existing `research_tool.py` pipeline?

Just say the word and I’ll extend it immediately. This setup gives your local LLM full programmatic control over a real graphical browser while staying extremely lightweight.