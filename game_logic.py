import random
import os

# --- Konfigurasi Permainan ---
BOARD_SIZE = 100
STATE_FILE = 'game_state.txt'
OUTPUT_SVG = 'game_board.svg'

# Definisikan posisi ular dan tangga
# Format: {posisi_awal: posisi_akhir}
SNAKES = {
    17: 7, 54: 34, 62: 19, 64: 60,
    87: 24, 93: 73, 95: 75, 99: 78
}
LADDERS = {
    4: 14, 9: 31, 20: 38, 28: 84,
    40: 59, 51: 67, 63: 81, 71: 91
}

# --- Logika Permainan ---

def get_current_position():
    """Membaca posisi saat ini dari file state."""
    if not os.path.exists(STATE_FILE):
        return 0
    with open(STATE_FILE, 'r') as f:
        try:
            return int(f.read().strip())
        except (ValueError, IndexError):
            return 0

def save_position(position):
    """Menyimpan posisi baru ke file state."""
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        f.write(str(position))

def generate_svg(position):
    """Membuat file SVG baru dengan posisi pion."""
    # Koordinat X, Y untuk setiap kotak (0-100)
    # Ini perlu disesuaikan dengan gambar papan Anda
    coords = {}
    for i in range(1, 101):
        row = (i - 1) // 10
        col = (i - 1) % 10
        if row % 2 != 0: # Baris ganjil (dari bawah), urutan dari kanan ke kiri
            x = 285 - (col * 30)
        else: # Baris genap, urutan dari kiri ke kanan
            x = 15 + (col * 30)
        y = 285 - (row * 30)
        coords[i] = (x, y)
    coords[0] = (-20, 285) # Posisi awal di luar papan

    pion_x, pion_y = coords.get(position, coords[0])

    # Template SVG dasar (papan permainan statis)
    # Anda bisa mengganti ini dengan SVG papan permainan kustom Anda
    svg_template = f'''
    <svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">
        <!-- Latar Belakang dan Garis -->
        <rect width="100%" height="100%" fill="#F7F7F7"/>
        <g id="grid">
            <!-- Membuat grid 10x10 -->
            <path stroke="#CCC" d="
                {' '.join([f'M {i*30},0 V 300' for i in range(1, 10)])}
                {' '.join([f'M 0,{i*30} H 300' for i in range(1, 10)])}
            "/>
        </g>
        <!-- Nomor Kotak -->
        <g id="numbers" font-size="8" font-family="sans-serif" text-anchor="middle">
            {''.join([f'<text x="{coords[i][0]}" y="{coords[i][1]+5}">{i}</text>' for i in range(1, 101)])}
        </g>
        <!-- Ular dan Tangga (visual sederhana) -->
        <g id="snakes_ladders" stroke-width="2">
            <!-- Tangga (hijau) -->
            {''.join([f'<line x1="{coords[start][0]}" y1="{coords[start][1]}" x2="{coords[end][0]}" y2="{coords[end][1]}" stroke="#4CAF50"/>' for start, end in LADDERS.items()])}
            <!-- Ular (merah) -->
            {''.join([f'<line x1="{coords[start][0]}" y1="{coords[start][1]}" x2="{coords[end][0]}" y2="{coords[end][1]}" stroke="#F44336"/>' for start, end in SNAKES.items()])}
        </g>
        <!-- Pion Pemain -->
        <text x="{pion_x}" y="{pion_y}" font-size="20">🚀</text>
    </svg>
    '''
    with open(OUTPUT_SVG, 'w', encoding='utf-8') as f:
        f.write(svg_template)

def main():
    """Fungsi utama untuk menjalankan permainan."""
    current_pos = get_current_position()
    dice_roll = random.randint(1, 6)
    
    new_pos = current_pos + dice_roll

    if new_pos > BOARD_SIZE:
        new_pos = current_pos # Jika lemparan melebihi 100, tetap di tempat
    elif new_pos in SNAKES:
        new_pos = SNAKES[new_pos]
    elif new_pos in LADDERS:
        new_pos = LADDERS[new_pos]

    if new_pos >= BOARD_SIZE:
        new_pos = BOARD_SIZE # Menang!
        # Reset permainan jika sudah menang
        save_position(0)
    else:
        save_position(new_pos)

    generate_svg(new_pos)
    
    # Mengatur output untuk GitHub Actions
    print(f"::set-output name=new_position::{new_pos}")

if __name__ == "__main__":
    main()
