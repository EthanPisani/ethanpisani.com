import * as THREE from 'https://threejsfundamentals.org/threejs/resources/threejs/r125/build/three.module.js';
import {OrbitControls} from 'https://threejsfundamentals.org/threejs/resources/threejs/r125/examples/jsm/controls/OrbitControls.js';
import {GLTFLoader} from 'https://threejsfundamentals.org/threejs/resources/threejs/r125/examples/jsm/loaders/GLTFLoader.js';
let camera, scene, renderer;

init();
render();

function init() {

    const container = document.createElement( 'div' );
    document.body.appendChild( container );

    camera = new THREE.PerspectiveCamera( 45, window.innerWidth / window.innerHeight, 0.25, 20 );
    //camera.position.set( - 1.8, 0.6, 2.7 );

    scene = new THREE.Scene();

            const loader = new GLTFLoader().setPath('../models/organic/' );
            var obj;
            //loader.load( 'propan-2-ol.glb', function ( gltf ) {
                loader.load( 'testmolctrlj.glb', function ( gltf ) {
                //loader.load( 'Box.gltf', function ( gltf ) {
                obj = gltf.scene;
                scene.add( gltf.scene );


                render();

            } );
            var light = new THREE.HemisphereLight(0xffffff, 0x000000, 1.5)
            scene.add(light);
            camera.position.set(0, 0, 10)
            scene.background = new THREE.Color(0x2c2c2c)
            //Object.rotation.y += 0.01;
    renderer = new THREE.WebGLRenderer( { antialias: true } );
    renderer.setPixelRatio( window.devicePixelRatio );
    renderer.setSize( window.innerWidth, window.innerHeight );
    container.appendChild( renderer.domElement );
    window.addEventListener( 'resize', onWindowResize );

    function animate(){
        requestAnimationFrame(animate);
        obj.rotation.y += 0.005;
        obj.rotation.z += 0.005;
        obj.rotation.x += 0.005;
        renderer.render(scene, camera)
    }
    animate();

    

}



function onWindowResize() {

    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize( window.innerWidth, window.innerHeight );

    render();

}

//

function render() {

    renderer.render( scene, camera );

}
