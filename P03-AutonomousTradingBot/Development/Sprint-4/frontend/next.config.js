module.exports = () => {
	const rewrites = () => {
		return [
			{
				source: '/api/:path*',
				// destination: 'http://127.0.0.1:5000/api/:path*',
				destination:
					'https://autonomous-trading-bot.el.r.appspot.com/api/:path*',
			},
		];
	};
	return {
		rewrites,
		images: {
			dangerouslyAllowSVG: true,
			domains: ['api.polygon.io'],
		},
	};
};
