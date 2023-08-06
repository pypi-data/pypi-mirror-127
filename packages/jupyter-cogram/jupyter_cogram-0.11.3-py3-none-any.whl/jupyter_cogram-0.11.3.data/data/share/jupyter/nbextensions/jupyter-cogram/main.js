const logPrefix = '[jupyter-cogram-sources-loader]';
const cdnUrl = 'https://storage.googleapis.com/cogram-public/jupyter-cogram/latest/cogram_main.min.js';

console.log(logPrefix, "Loading Jupyter extension from CDN URL", cdnUrl)

define([cdnUrl,], function (cogram) {
    "use strict";
    console.log(logPrefix, "Loaded `cogram` module")
    return {
        load_jupyter_extension: cogram.load_jupyter_extension,
        load_ipython_extension: cogram.load_jupyter_extension
    };
});
