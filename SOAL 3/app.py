<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Jurnal Kas Keluar</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; }
    </style>
</head>
<body class="bg-slate-50 min-h-screen py-8 px-4 sm:px-6 lg:px-8">
    <div class="max-w-5xl mx-auto bg-white rounded-2xl shadow-xl overflow-hidden border border-slate-100">
        
        <!-- Header Section -->
        <div class="bg-gradient-to-r from-blue-600 to-indigo-700 px-6 py-6 text-white">
            <h1 class="text-2xl font-bold tracking-tight">Form Jurnal Kas Keluar</h1>
            <p class="text-blue-100 text-sm mt-1">Catat transaksi pengeluaran kas dengan validasi balance otomatis.</p>
        </div>

        <!-- Form Body -->
        <form id="journalForm" class="p-6 sm:p-8 space-y-6" onsubmit="handleSubmit(event)">
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- Tanggal -->
                <div>
                    <label class="block text-sm font-semibold text-slate-700 mb-2">Tanggal</label>
                    <input type="date" id="docDate" required 
                        class="w-full rounded-xl border border-slate-300 px-4 py-2.5 text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition">
                </div>
                <!-- Nomor Referensi -->
                <div>
                    <label class="block text-sm font-semibold text-slate-700 mb-2">No. Referensi</label>
                    <input type="text" id="docRef" placeholder="Cth: BKK-2026-001" required 
                        class="w-full rounded-xl border border-slate-300 px-4 py-2.5 text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition">
                </div>
                <!-- Deskripsi Header -->
                <div>
                    <label class="block text-sm font-semibold text-slate-700 mb-2">Deskripsi Umum</label>
                    <input type="text" id="docDesc" placeholder="Keterangan pengeluaran..." required 
                        class="w-full rounded-xl border border-slate-300 px-4 py-2.5 text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition">
                </div>
            </div>

            <div class="pt-4">
                <div class="flex items-center justify-between mb-3">
                    <h2 class="text-lg font-bold text-slate-800">Baris Jurnal</h2>
                    <button type="button" onclick="addRow()" 
                        class="inline-flex items-center space-x-1 bg-emerald-600 hover:bg-emerald-700 text-white text-sm font-medium px-4 py-2 rounded-xl shadow-sm transition transform active:scale-95">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path></svg>
                        <span>Tambah Baris</span>
                    </button>
                </div>

                <div class="overflow-x-auto rounded-xl border border-slate-200">
                    <table class="min-w-full divide-y divide-slate-200">
                        <thead class="bg-slate-100 text-slate-700 uppercase text-xs font-semibold tracking-wider">
                            <tr>
                                <th class="px-4 py-3 text-left w-2/5">Akun</th>
                                <th class="px-4 py-3 text-right w-1/4">Debit (Rp)</th>
                                <th class="px-4 py-3 text-right w-1/4">Kredit (Rp)</th>
                                <th class="px-4 py-3 text-center w-10">Aksi</th>
                            </tr>
                        </thead>
                        <tbody id="journalRows" class="bg-white divide-y divide-slate-200">
                            <!-- Dynamic rows appended via JS -->
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="bg-slate-50 p-4 sm:p-6 rounded-2xl border border-slate-200 flex flex-col md:flex-row justify-between items-center gap-4">
                <div class="w-full md:w-auto space-y-1 text-center md:text-left">
                    <div id="warningBox" class="text-rose-600 font-semibold text-sm hidden bg-rose-50 border border-rose-200 px-4 py-2 rounded-xl">
                        ⚠️ Jurnal belum balance atau nilai total masih 0!
                    </div>
                    <div id="successBox" class="text-emerald-600 font-semibold text-sm hidden bg-emerald-50 border border-emerald-200 px-4 py-2 rounded-xl">
                        ✨ Jurnal balance dan siap disimpan!
                    </div>
                </div>

                <div class="grid grid-cols-3 gap-4 text-right w-full md:w-auto">
                    <div class="bg-white p-3 rounded-xl border border-slate-200 shadow-sm">
                        <div class="text-xs text-slate-500 font-medium">Total Debit</div>
                        <div id="totalDebit" class="text-base sm:text-lg font-bold text-slate-800">Rp 0</div>
                    </div>
                    <div class="bg-white p-3 rounded-xl border border-slate-200 shadow-sm">
                        <div class="text-xs text-slate-500 font-medium">Total Kredit</div>
                        <div id="totalKredit" class="text-base sm:text-lg font-bold text-slate-800">Rp 0</div>
                    </div>
                    <div class="bg-white p-3 rounded-xl border border-slate-200 shadow-sm">
                        <div class="text-xs text-slate-500 font-medium">Selisih (D - K)</div>
                        <div id="totalSelisih" class="text-base sm:text-lg font-bold text-amber-600">Rp 0</div>
                    </div>
                </div>
            </div>

            <div class="flex items-center justify-end pt-4 border-t border-slate-100">
                <button type="submit" id="submitBtn" disabled
                    class="bg-blue-600 text-white font-semibold px-8 py-3 rounded-xl shadow-lg hover:bg-blue-700 transition transform active:scale-95 disabled:bg-slate-300 disabled:cursor-not-allowed disabled:shadow-none">
                    Simpan Jurnal
                </button>
            </div>
        </form>
    </div>

    <!-- Custom Modal instead of alert -->
    <div id="customModal" class="fixed inset-0 bg-slate-900/50 backdrop-blur-sm hidden items-center justify-center z-50 p-4">
        <div class="bg-white rounded-2xl max-w-sm w-full p-6 text-center shadow-2xl border border-slate-100">
            <div class="w-12 h-12 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
            </div>
            <h3 class="text-lg font-bold text-slate-800 mb-2">Berhasil!</h3>
            <p id="modalMessage" class="text-sm text-slate-600 mb-6">Data jurnal kas keluar berhasil disimpan.</p>
            <button onclick="closeModal()" class="w-full bg-slate-900 text-white py-2.5 rounded-xl font-medium hover:bg-slate-800 transition">Tutup</button>
        </div>
    </div>

    <script>
        // Daftar akun contoh untuk dropdown
        const accountList = [
            "1-1100 - Kas di Bank",
            "1-1200 - Kas Kecil",
            "2-1100 - Hutang Usaha",
            "5-1100 - Beban Gaji",
            "5-1200 - Beban Sewa Kantor",
            "5-1300 - Beban Listrik & Air",
            "5-1400 - Beban Perlengkapan"
        ];

        // Set default tanggal hari ini
        document.getElementById('docDate').valueAsDate = new Date();

        // Inisialisasi awal dengan 2 baris
        window.onload = function() {
            addRow();
            addRow();
            calculateTotals();
        };

        // Fungsi menambah baris baru ke tabel
        function addRow() {
            const tbody = document.getElementById('journalRows');
            const tr = document.createElement('tr');
            tr.className = 'hover:bg-slate-50/50 transition';

            let optionsHtml = accountList.map(acc => `<option value="${acc}">${acc}</option>`).join('');

            tr.innerHTML = `
                <td class="px-4 py-3">
                    <select class="account-select w-full rounded-lg border border-slate-300 px-3 py-2 text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white text-sm">
                        ${optionsHtml}
                    </select>
                </td>
                <td class="px-4 py-3">
                    <input type="number" min="0" value="0" oninput="calculateTotals()" 
                        class="debit-input w-full rounded-lg border border-slate-300 px-3 py-2 text-right text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm">
                </td>
                <td class="px-4 py-3">
                    <input type="number" min="0" value="0" oninput="calculateTotals()" 
                        class="kredit-input w-full rounded-lg border border-slate-300 px-3 py-2 text-right text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm">
                </td>
                <td class="px-4 py-3 text-center">
                    <button type="button" onclick="deleteRow(this)" 
                        class="text-slate-400 hover:text-rose-600 transition p-1.5 rounded-lg hover:bg-rose-50">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2.000 2.000 0 0116.138 21H7.862a2.000 2.000 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
                    </button>
                </td>
            `;
            tbody.appendChild(tr);
            calculateTotals();
        }

        // Fungsi menghapus baris (minimal menyisakan 1 baris)
        function deleteRow(btn) {
            const tbody = document.getElementById('journalRows');
            if (tbody.rows.length > 1) {
                btn.closest('tr').remove();
                calculateTotals();
            } else {
                showCustomModal("Minimal harus ada 1 baris jurnal!");
            }
        }

        // Format angka ke format mata uang Rupiah
        function formatRupiah(amount) {
            return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', minimumFractionDigits: 0 }).format(amount);
        }

        // Kalkulasi total debit, kredit, selisih & validasi tombol submit
        function calculateTotals() {
            const debitInputs = document.querySelectorAll('.debit-input');
            const kreditInputs = document.querySelectorAll('.kredit-input');

            let totalDebit = 0;
            let totalKredit = 0;

            debitInputs.forEach(input => {
                let val = parseFloat(input.value) || 0;
                totalDebit += val;
            });

            kreditInputs.forEach(input => {
                let val = parseFloat(input.value) || 0;
                totalKredit += val;
            });

            let selisih = totalDebit - totalKredit;

            // Render ke UI
            document.getElementById('totalDebit').innerText = formatRupiah(totalDebit);
            document.getElementById('totalKredit').innerText = formatRupiah(totalKredit);
            document.getElementById('totalSelisih').innerText = formatRupiah(selisih);

            const submitBtn = document.getElementById('submitBtn');
            const warningBox = document.getElementById('warningBox');
            const successBox = document.getElementById('successBox');

            // Cek kondisi balance & > 0
            if (totalDebit > 0 && totalDebit === totalKredit) {
                submitBtn.disabled = false;
                warningBox.classList.add('hidden');
                successBox.classList.remove('hidden');
            } else {
                submitBtn.disabled = true;
                warningBox.classList.remove('hidden');
                successBox.classList.add('hidden');
            }
        }

        // Handler submit form
        function handleSubmit(event) {
            event.preventDefault();
            const date = document.getElementById('docDate').value;
            const ref = document.getElementById('docRef').value;
            const desc = document.getElementById('docDesc').value;
            
            showCustomModal(`Jurnal dengan referensi ${ref} bertanggal ${date} berhasil disimpan.`);
            // Reset form jika diinginkan
            document.getElementById('journalForm').reset();
            document.getElementById('docDate').valueAsDate = new Date();
            document.getElementById('journalRows').innerHTML = '';
            addRow();
            addRow();
            calculateTotals();
        }

        // Modal kustom pengganti alert
        function showCustomModal(message) {
            document.getElementById('modalMessage').innerText = message;
            document.getElementById('customModal').classList.remove('hidden');
            document.getElementById('customModal').classList.add('flex');
        }

        function closeModal() {
            document.getElementById('customModal').classList.remove('flex');
            document.getElementById('customModal').classList.add('hidden');
        }
    </script>
</body>
</html>