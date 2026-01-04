// API Configuration
// When accessing from another device on the network, use your local IP
// When accessing locally, use localhost

const getApiUrl = () => {
    // Check if we're in browser environment
    if (typeof window !== 'undefined') {
        // In local development, if we're using static export (output: 'export'),
        // rewrites in next.config.js might not work.
        // So we use the absolute URL for the backend if we are on localhost.
        if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            return 'http://localhost:8000';
        }

        // Use the Render backend URL for production
        return 'https://cinenest-backend.onrender.com';
    }

    // Default to localhost for local env, or use Env var for production build
    return process.env.NEXT_PUBLIC_API_URL || 'https://cinenest-backend.onrender.com';
};

export const API_URL = getApiUrl();
