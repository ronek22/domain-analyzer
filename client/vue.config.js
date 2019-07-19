const path = require("path");

module.exports = {
    outputDir: path.resolve(__dirname, "../server/templates"),
    assetsDir: 'static',
    devServer: {
        proxy: {
            "/": {
                target: "http://localhost:5000",
                ws: false,
                changeOrigin: true
            }
        }
    }
}