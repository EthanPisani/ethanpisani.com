import * as THREE from 'https://threejsfundamentals.org/threejs/resources/threejs/r125/build/three.module.js';
import {OrbitControls} from 'https://threejsfundamentals.org/threejs/resources/threejs/r125/examples/jsm/controls/OrbitControls.js';
import {GLTFLoader} from 'https://threejsfundamentals.org/threejs/resources/threejs/r125/examples/jsm/loaders/GLTFLoader.js';
const loader = new GLTFLoader();
const scene = new THREE.Scene();
//scene.background = new THREE.Color('black');
// Load a glTF resource




const gltfLoader = new GLTFLoader();
    gltfLoader.load('../models/organic/propan-2-ol.gltf', (gltf) => {
      const root = gltf.scene;
      scene.add(root);
      gltf.asset;
      render();
    });