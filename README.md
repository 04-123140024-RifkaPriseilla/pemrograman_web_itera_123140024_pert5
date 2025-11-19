## Rifka Priseilla Br Silitonga (123140024)

# Sistem Manajemen Perpustakaan (Python OOP)

## Penjelasan Program
Program ini merupakan sistem manajemen perpustakaan sederhana yang dibuat menggunakan konsep **OOP Python**, termasuk:
- **Abstract Class**
- **Inheritance**
- **Encapsulation**
- **Polymorphism**
- **Property Decorator**

Program mampu:
- Menambahkan item (Buku & Majalah) ke perpustakaan
- Menampilkan daftar item
- Mencari item berdasarkan judul atau ID

---

## Fitur Utama
1. **LibraryItem (Abstract Class)**  
   Menjadi dasar untuk semua item perpustakaan dengan method `display_info()`.

2. **Book & Magazine (Subclass)**  
   Meng-override method abstract untuk menampilkan detail masing-masing item.

3. **Library Class**  
   Mengelola koleksi item menggunakan list privat (`__items`).

4. **Encapsulation**  
   Atribut penting menggunakan protected (`_item_id`) dan private (`__author`).

5. **Polymorphism**  
   Method `display_info()` berperilaku berbeda pada tiap subclass.

---

## Screenshot Output (Simulasi)
![Screenshot Output](screenshot/HasilSimulasi.png)


---

## Diagram Class (UML)
![Class Diagram](screenshot/ClassDiagram.png)
