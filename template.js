/**
 * Avatar Processing Service - Coding Challenge Template (Simplified)
 * 
 * Choose your preferred language and adapt this structure accordingly.
 * This JavaScript template can be converted to Python, Go, Java, etc.
 * 
 * Mock LLM API Endpoint:
 * POST /api/v1/moderate-content
 * Headers: Authorization: Bearer <token>
 * Body: {
 *   "content": "description of the generated avatar",
 *   "user_id": "user123"
 * }
 * 
 * Response: {
 *   "approved": true,
 *   "reason": "Content appears safe"
 * }
 */

const { randomUUID } = require('crypto');

/**
 * @typedef {Object} ModerationResponse
 * @property {boolean} isApproved
 * @property {string} [reason]
 */

/**
 * Avatar job data structure
 */
class AvatarJob {
    /**
     * @param {string} id - Unique job identifier
     * @param {string} userId - User ID who requested the avatar
     * @param {string} status - Job status: pending, completed, failed, rejected
     * @param {string} inputData - User's avatar prompt
     * @param {string} [outputUrl] - Generated avatar URL
     * @param {Date} [createdAt] - Job creation timestamp
     * @param {string} [errorMessage] - Error message if job failed
     */
    constructor(id, userId, status, inputData, outputUrl = null, createdAt = null, errorMessage = null) {
        this.id = id;
        this.userId = userId;
        this.status = status;
        this.inputData = inputData;
        this.outputUrl = outputUrl;
        this.createdAt = createdAt || new Date();
        this.errorMessage = errorMessage;
    }
}

class AvatarProcessingService {
    /**
     * Initialize the avatar processing service.
     * 
     * @param {string} moderationApiUrl - Base URL for the moderation API
     * @param {string} apiToken - Bearer token for API authentication
     */
    constructor(moderationApiUrl, apiToken) {
        this.moderationApiUrl = moderationApiUrl;
        this.apiToken = apiToken;
        // TODO: Initialize your storage, HTTP client, etc.
    }

    /**
     * Submit a new avatar generation job and process it synchronously.
     * 
     * @param {string} userId - ID of the user requesting the avatar
     * @param {string} inputData - User's avatar generation prompt/description
     * @returns {Promise<AvatarJob>} The completed job object
     * 
     * Should:
     * 1. Create a new job with unique ID
     * 2. Generate a mock avatar URL
     * 3. Call moderation API
     * 4. Update job status based on moderation result
     * 5. Store and return the job
     */
    async submitJob(userId, inputData) {
        // TODO: Implement job creation and full processing
    }

    /**
     * Retrieve the current status of a job.
     * 
     * @param {string} jobId - ID of the job to check
     * @returns {AvatarJob|null} The job object if found, null otherwise
     */
    getJobStatus(jobId) {
        // TODO: Implement job retrieval from storage
    }

    /**
     * Call the content moderation API to check if avatar passes guidelines.
     * 
     * @param {string} content - Description of the generated avatar
     * @param {string} userId - ID of the user who requested the avatar
     * @returns {Promise<ModerationResponse>} Moderation result
     * 
     * Should:
     * - Make HTTP POST request to moderation API
     * - Handle timeouts and basic errors
     * - Parse response into ModerationResponse object
     * - Optional: Add simple retry logic
     */
    async callModerationApi(content, userId) {
        // TODO: Implement HTTP client call with error handling
    }

    /**
     * Generate a mock avatar URL (simulate avatar generation).
     * 
     * @param {string} prompt - User's avatar description
     * @returns {string} Mock URL to the generated avatar
     */
    _generateMockAvatarUrl(prompt) {
        // TODO: Return a mock URL like "https://avatars.example.com/avatar_123.png"
    }
}

// Example usage and testing
async function main() {
    /**
     * Example usage of the avatar processing service.
     * You can use this to test your implementation.
     */
    const service = new AvatarProcessingService(
        "https://api.example.com",
        "your-api-token-here"
    );
    
    // Submit a job
    const job = await service.submitJob("user123", "A friendly robot avatar with blue eyes");
    console.log(`Job submitted: ${job.id}, Status: ${job.status}`);
    
    // Check status
    const retrievedJob = service.getJobStatus(job.id);
    console.log(`Retrieved job status: ${retrievedJob ? retrievedJob.status : 'Not found'}`);
}

if (require.main === module) {
    main().catch(console.error);
}

module.exports = { AvatarJob, AvatarProcessingService };

/**
 * IMPLEMENTATION NOTES:
 * 
 * 1. Storage: Use a simple in-memory Map or Object
 *    - jobs = new Map()  // jobId -> AvatarJob
 *    - or jobs = {}      // jobId -> AvatarJob
 * 
 * 2. HTTP Client: Use fetch (Node.js 18+) or axios
 *    - Set timeout (e.g., 5 seconds)
 *    - Handle basic HTTP errors
 * 
 * 3. Error Handling: Focus on:
 *    - API timeout
 *    - API returns error status
 *    - Network issues
 *    - Invalid response format
 * 
 * 4. Job Flow:
 *    - Create job with "pending" status
 *    - Generate mock avatar URL
 *    - Call moderation API
 *    - Update status to "completed" or "rejected"
 *    - Handle errors by setting status to "failed"
 * 
 * 5. Mock Avatar URL: 
 *    - Return something like `https://avatars.example.com/${jobId}.png`
 * 
 * 6. Keep It Simple:
 *    - Synchronous processing is fine
 *    - Basic error handling is sufficient
 *    - Focus on the API integration
 * 
 * 7. Node.js Specific:
 *    - Use require('crypto').randomUUID() for unique IDs
 *    - Use built-in fetch() for HTTP requests (Node 18+)
 *    - Or install axios: npm install axios
 */ 