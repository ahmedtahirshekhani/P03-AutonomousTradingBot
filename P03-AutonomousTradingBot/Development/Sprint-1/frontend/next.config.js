module.exports = () => {
  const rewrites = () => {
    return [
      {
        source: "/api/:path*",
        destination: "https://autonomous-trading-bot.el.r.appspot.com/:path*",
      },
    ];
  };
  return {
    rewrites,
  };
};