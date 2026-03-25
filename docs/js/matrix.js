const canvas = document.getElementById('matrix');
const ctx = canvas.getContext('2d', { alpha: false });

let width, height;
const fontSize = 32; 
const chars = 'ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾖﾗﾘﾙﾚﾛﾜﾝ1234567890';

let mouseX = -1000, mouseY = -1000;
let rippleRadius = 0, isRippling = false;
let grid = []; 
let columns = []; 
let audioCtx;

function initAudio() {
    if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
}

function playWhoosh() {
    if (!audioCtx) return;
    const osc = audioCtx.createOscillator();
    const g = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(180, audioCtx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(20, audioCtx.currentTime + 1.2);
    g.gain.setValueAtTime(0.2, audioCtx.currentTime);
    g.gain.linearRampToValueAtTime(0, audioCtx.currentTime + 1.2);
    osc.connect(g).connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + 1.2);
}

function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
    const cols = Math.ceil(width / (fontSize * 1.6));
    const rows = Math.ceil(height / fontSize);
    
    grid = [];
    for (let y = 0; y < rows; y++) {
        grid[y] = [];
        for (let x = 0; x < cols; x++) {
            grid[y][x] = { char: chars[Math.floor(Math.random() * chars.length)], opacity: 0 };
        }
    }

    columns = [];
    for (let i = 0; i < cols; i++) {
        columns.push({
            x: i,
            y: Math.random() * rows,
            speed: 0.08 + Math.random() * 0.12,
            fadeSpeed: 0.002 + Math.random() * 0.007 
        });
    }
}

window.addEventListener('resize', resize);
window.addEventListener('mousemove', (e) => { mouseX = e.clientX; mouseY = e.clientY; });
window.addEventListener('mousedown', () => {
    initAudio();
    rippleRadius = 0;
    isRippling = true;
    playWhoosh();
});

function draw() {
    ctx.fillStyle = 'black';
    ctx.fillRect(0, 0, width, height);

    const holeRadius = 260;
    const glowZone = 360;

    if (isRippling) {
        rippleRadius += 18;
        if (rippleRadius > width * 1.5) isRippling = false;
    }

    columns.forEach(col => {
        col.y += col.speed;
        if (col.y >= grid.length) col.y = 0;
        const currentRow = Math.floor(col.y);
        if (grid[currentRow] && grid[currentRow][col.x]) {
            grid[currentRow][col.x].opacity = 1.0;
        }
    });

    for (let y = 0; y < grid.length; y++) {
        for (let x = 0; x < grid[y].length; x++) {
            const cell = grid[y][x];
            if (cell.opacity <= 0) continue;

            const baseX = x * (fontSize * 1.6);
            const baseY = y * fontSize + fontSize;
            const dx = mouseX - baseX, dy = mouseY - baseY;
            const distance = Math.sqrt(dx * dx + dy * dy);

            let drawX = baseX, drawY = baseY, currentSize = fontSize, currentOpacity = cell.opacity;
            let colorBase = [25, 80, 35];

            if (distance < glowZone) {
                const glowForce = (glowZone - distance) / glowZone;
                colorBase[0] += glowForce * 80; colorBase[1] += glowForce * 160; colorBase[2] += glowForce * 60;
                if (distance < holeRadius) {
                    const pullForce = (holeRadius - distance) / holeRadius;
                    drawX += dx * pullForce * 0.92;
                    drawY += dy * pullForce * 0.92;
                    currentSize *= (1 - pullForce * 0.88);
                    currentOpacity *= (1 - pullForce);
                }
            }

            if (isRippling) {
                const rw = 80;
                if (distance > rippleRadius - rw && distance < rippleRadius + rw) {
                    const rf = 1 - Math.abs(distance - rippleRadius) / rw;
                    drawX -= (dx / distance) * rf * 80;
                    drawY -= (dy / distance) * rf * 80;
                    colorBase = [100, 255, 150];
                    currentOpacity = Math.min(1, currentOpacity + 0.5);
                }
            }

            if (currentOpacity > 0.02) {
                ctx.save();
                ctx.translate(drawX, drawY);
                ctx.scale(1.7, 1.0); 
                ctx.font = `bold ${currentSize}px monospace`;
                ctx.fillStyle = `rgba(${colorBase[0]}, ${colorBase[1]}, ${colorBase[2]}, ${currentOpacity})`;
                if (Math.random() > 0.99) cell.char = chars[Math.floor(Math.random() * chars.length)];
                ctx.fillText(cell.char, 0, 0);
                ctx.restore();
            }
            cell.opacity -= columns[x].fadeSpeed; 
        }
    }

    const pointerGlow = ctx.createRadialGradient(mouseX, mouseY, 0, mouseX, mouseY, 40);
    pointerGlow.addColorStop(0, 'rgba(0, 255, 120, 0.4)');
    pointerGlow.addColorStop(1, 'rgba(0, 0, 0, 0)');
    ctx.fillStyle = pointerGlow;
    ctx.beginPath(); ctx.arc(mouseX, mouseY, 40, 0, Math.PI * 2); ctx.fill();

    ctx.fillStyle = 'white';
    ctx.beginPath(); ctx.arc(mouseX, mouseY, 3, 0, Math.PI * 2); ctx.fill();

    requestAnimationFrame(draw);
}

resize();
requestAnimationFrame(draw);