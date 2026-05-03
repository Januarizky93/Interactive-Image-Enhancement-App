import tkinter as tk
from tkinter import filedialog, messagebox, Scale, DoubleVar
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.stats import entropy


class DigitalImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ADVANCED IMAGE PROCESSING - ADHITYA JANUARIZKY - 14240045")
        self.root.geometry("1700x950")

        # ================= DATA IMAGE =================
        self.original_display = None    
        self.original_gray = None        
        self.reference_gray = None

        # ================= HEADER =================
        header = tk.Frame(root, bg="white", height=80)
        header.pack(fill="x")
        tk.Label(
            header,
            text="ADVANCED IMAGE PROCESSING - ADHITYA JANUARIZKY - 14240045",
            font=("Helvetica", 22, "bold"),
            bg="white"
        ).pack(pady=20)

        # ================= MAIN =================
        main = tk.Frame(root)
        main.pack(fill="both", expand=True)

        # ================= LEFT PANEL =================
        left = tk.Frame(main, width=300, bg="#145A32", padx=10, pady=10)
        left.pack(side="left", fill="y")
        left.pack_propagate(False)

        tk.Button(left, text="Open Image", bg="#A93226", fg="white",
                  height=2, command=self.open_image).pack(fill="x", pady=5)

        tk.Button(left, text="Open Reference Image", bg="#A93226", fg="white",
                  height=2, command=self.open_reference).pack(fill="x", pady=5)

        self.gamma = DoubleVar(value=1.0)
        tk.Label(left, text="Gamma Value", fg="white", bg="#145A32").pack(pady=(15, 0))
        Scale(left, from_=0.1, to=5.0, resolution=0.1,
              orient="horizontal", variable=self.gamma,
              bg="#145A32", fg="white").pack(fill="x")

        # ================= RIGHT PANEL =================
        right = tk.Frame(main, width=320, bg="#145A32", padx=10, pady=10)
        right.pack(side="right", fill="y")
        right.pack_propagate(False)

        def btn(text, cmd):
            return tk.Button(right, text=text, command=cmd,
                             bg="#A93226", fg="white", height=2)

        tk.Label(right, text="Transformasi Intensitas",
                 fg="white", bg="#145A32",
                 font=("Helvetica", 12, "bold")).pack(pady=5)

        btn("Image Negative", self.image_negative).pack(fill="x", pady=3)
        btn("Power Law", self.power_law).pack(fill="x", pady=3)
        btn("Gray Level Slicing", self.gray_slicing).pack(fill="x", pady=3)

        tk.Label(right, text="Analisis Histogram",
                 fg="white", bg="#145A32",
                 font=("Helvetica", 12, "bold")).pack(pady=10)

        btn("Histogram", self.show_histogram).pack(fill="x", pady=3)
        btn("Histogram Equalization", self.histogram_equalization).pack(fill="x", pady=3)
        btn("Histogram Matching", self.histogram_matching).pack(fill="x", pady=3)
        btn("CLAHE", self.clahe).pack(fill="x", pady=3)

        # ================= DISPLAY =================
        self.fig = plt.figure(figsize=(14, 8))
        self.canvas = FigureCanvasTkAgg(self.fig, main)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self.show_message("Klik 'Open Image' untuk memulai")

    # ================= UTIL =================
    def show_message(self, text):
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.text(0.5, 0.5, text, fontsize=18, ha="center", va="center")
        ax.axis("off")
        self.canvas.draw()

    # ================= IMAGE LOADER (FIX TIFF USC SIPI) =================
    def open_image(self):
        path = filedialog.askopenfilename()
        if not path:
            return

        # === FILE TIFF (USC SIPI) ===
        if path.lower().endswith((".tif", ".tiff")):
            img_cv = cv2.imread(path, cv2.IMREAD_UNCHANGED)
            if img_cv is None:
                messagebox.showerror("Error", "Gambar TIFF tidak dapat dibaca")
                return

            if len(img_cv.shape) == 2:  # grayscale
                self.original_gray = cv2.resize(img_cv, (512, 512))
                self.original_display = self.original_gray.copy()
            else:  # color
                img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
                self.original_display = cv2.resize(img_rgb, (512, 512))
                self.original_gray = cv2.cvtColor(self.original_display, cv2.COLOR_RGB2GRAY)

        # === FILE NON-TIFF (JPG / PNG) ===
        else:
            img_pil = Image.open(path).resize((512, 512))
            self.original_display = np.array(img_pil)
            if img_pil.mode == "L":
                self.original_gray = np.array(img_pil)
            else:
                self.original_gray = np.array(img_pil.convert("L"))

        self.show_single(self.original_display, "Original Image")

    def open_reference(self):
        path = filedialog.askopenfilename()
        if not path:
            return

        img_cv = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img_cv is None:
            messagebox.showerror("Error", "Reference image tidak dapat dibaca")
            return

        self.reference_gray = cv2.resize(img_cv, (512, 512))
        messagebox.showinfo("Info", "Reference image loaded")

    # ================= STATISTIK =================
    def image_stats(self, img):
        hist = cv2.calcHist([img], [0], None, [256], [0, 256]).ravel()
        hist_norm = hist / hist.sum()
        return np.mean(img), entropy(hist_norm + 1e-12)

    # ================= DISPLAY CORE =================
    def display_result(self, processed, title, description, reference=None):
        gray = self.original_gray

        hist_o = cv2.calcHist([gray], [0], None, [256], [0, 256])
        hist_p = cv2.calcHist([processed], [0], None, [256], [0, 256])

        mean_o, ent_o = self.image_stats(gray)
        mean_p, ent_p = self.image_stats(processed)

        self.fig.clear()

        # IMAGES
        ax1 = self.fig.add_subplot(3, 2, 1)
        if self.original_display.ndim == 3:
            ax1.imshow(self.original_display)
        else:
            ax1.imshow(self.original_display, cmap="gray")
        ax1.set_title("Original Image")
        ax1.axis("off")

        ax2 = self.fig.add_subplot(3, 2, 2)
        ax2.imshow(processed, cmap="gray")
        ax2.set_title(title)
        ax2.axis("off")

        # HISTOGRAM
        ax3 = self.fig.add_subplot(3, 2, 3)
        ax3.plot(hist_o, color="#1f77b4")
        ax3.set_title("Histogram Original")

        ax4 = self.fig.add_subplot(3, 2, 4)
        ax4.plot(hist_p, color="#ff7f0e", label="Processed")
        if reference is not None:
            hist_r = cv2.calcHist([reference], [0], None, [256], [0, 256])
            ax4.plot(hist_r, color="#2ca02c", label="Reference")
            ax4.legend()
        ax4.set_title("Histogram Processed")

        # DESCRIPTION
        ax5 = self.fig.add_subplot(3, 1, 3)
        ax5.axis("off")
        ax5.text(
            0.01, 0.85,
            f"Keterangan:\n{description}\n\n"
            f"Statistik:\n"
            f"Mean Original = {mean_o:.2f}, Entropy Original = {ent_o:.3f}\n"
            f"Mean Hasil = {mean_p:.2f}, Entropy Hasil = {ent_p:.3f}",
            fontsize=11, va="top"
        )

        self.fig.tight_layout()
        self.canvas.draw()

    # ================= METHODS =================
    def image_negative(self):
        out = 255 - self.original_gray
        self.display_result(out, "Image Negative",
            "Transformasi negatif membalik intensitas piksel sehingga area terang menjadi gelap dan sebaliknya.")

    def power_law(self):
        g = self.gamma.get()
        out = np.clip(255 * (self.original_gray / 255) ** g, 0, 255).astype(np.uint8)
        self.display_result(out, f"Power Law (γ={g})",
            "Power-law (gamma correction) mengatur kecerahan citra secara non-linear.")

    def gray_slicing(self):
        out = np.zeros_like(self.original_gray)
        out[(self.original_gray >= 80) & (self.original_gray <= 180)] = 255
        self.display_result(out, "Gray Level Slicing",
            "Gray level slicing menonjolkan rentang intensitas tertentu.")

    def show_histogram(self):
        hist = cv2.calcHist([self.original_gray], [0], None, [256], [0, 256])
        mean, ent = self.image_stats(self.original_gray)

        self.fig.clear()
        ax1 = self.fig.add_subplot(2, 2, 1)
        if self.original_display.ndim == 3:
            ax1.imshow(self.original_display)
        else:
            ax1.imshow(self.original_display, cmap="gray")
        ax1.axis("off")

        ax2 = self.fig.add_subplot(2, 2, 2)
        ax2.plot(hist, color="#1f77b4")
        ax2.set_title("Histogram Grayscale")

        ax3 = self.fig.add_subplot(2, 1, 2)
        ax3.axis("off")
        ax3.text(0.01, 0.8, f"Mean = {mean:.2f}\nEntropy = {ent:.3f}", fontsize=11)

        self.canvas.draw()

    def histogram_equalization(self):
        out = cv2.equalizeHist(self.original_gray)
        self.display_result(out, "Histogram Equalization",
            "Histogram equalization meningkatkan kontras global citra.")

    def histogram_matching(self):
        if self.reference_gray is None:
            messagebox.showerror("Error", "Load reference image first")
            return

        src = self.original_gray
        ref = self.reference_gray

        hist_s, _ = np.histogram(src.flatten(), 256, [0, 256])
        hist_r, _ = np.histogram(ref.flatten(), 256, [0, 256])
        cdf_s = hist_s.cumsum() / hist_s.sum()
        cdf_r = hist_r.cumsum() / hist_r.sum()
        lut = np.interp(cdf_s, cdf_r, np.arange(256))
        out = lut[src].astype(np.uint8)

        self.display_result(out, "Histogram Matching",
            "Histogram matching menyesuaikan distribusi intensitas citra sumber dengan citra referensi.",
            reference=ref)

    def clahe(self):
        out = cv2.createCLAHE(2.0, (8, 8)).apply(self.original_gray)
        self.display_result(out, "CLAHE",
            "CLAHE meningkatkan kontras dan detail lokal tanpa over-enhancement.")

    def show_single(self, img, title):
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        if img.ndim == 3:
            ax.imshow(img)
        else:
            ax.imshow(img, cmap="gray")
        ax.set_title(title)
        ax.axis("off")
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalImageProcessingApp(root)
    root.mainloop()
