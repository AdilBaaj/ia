const webpack = require('webpack');
const WebpackDevServer = require('webpack-dev-server');
const config = require('./webpack.config');

new WebpackDevServer(webpack(config), {
  publicPath: config.output.publicPath,
  hot: true,
  historyApiFallback: true
}).listen(80, '0.0.0.0', (err) => {
  if (err) {
    console.log(err);
  }
  console.log('Listening at 0.0.0.0:80');
});
