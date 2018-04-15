var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  entry: {
    // Add as many entry points as you have container-react-components here
    App1: './reactjs/App1',
  },
  output: {
      path: path.resolve('./static/bundles/local/'),
      filename: "[name]-[hash].js"
  },

  mode: 'production',

  plugins: [
    new BundleTracker({filename: './webpack-stats-local.json'}),
  ],


  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },
}