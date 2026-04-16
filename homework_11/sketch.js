function faceCanvas(p) {
    p.setup = function() {
        let canvas = p.createCanvas(400, 600);
        canvas.parent('face');
    };

    let cooldown = 1;
    var cooldown_timer = 0;
    var simulation = new FaceSim(8, 12, 50, 630);

    p.draw = function() {
        if (cooldown_timer == 0) {
            cooldown_timer = cooldown;
            simulation.spawnCircle();
        } else {
            cooldown_timer--;
        }

        simulation.oscillateSpawner();

        simulation.applySpeedAndGravity();
        simulation.buildGrid();

        for (let samples = 0; samples < 20; samples++) {
            simulation.physicsStep();
            simulation.enforceBounds();
        }

        p.background(48, 54, 51);
        p.strokeWeight(0);

        for (let i = 0; i < simulation.circles.length; i++) {
            let circle = simulation.circles[i];

            p.fill(circle.color);
            p.circle(circle.x, circle.y, circle.radius * 2);
        }
    };
}

new p5(faceCanvas);