/*
Avatar Processing Service - Coding Challenge Template (Simplified)

IMPLEMENTATION NOTES:

1. Storage: Use a simple in-memory map

2. HTTP Client: Use standard library net/http
   - Set timeout (e.g., 5 seconds)
   - Handle basic HTTP errors

3. Error Handling: Focus on:
   - API timeout
   - API returns error status
   - Network issues
   - Invalid response format

4. Job Flow:
   - Create job with "pending" status
   - Generate mock avatar URL
   - Call moderation API
   - Update status to "completed" or "rejected"
   - Handle errors by setting status to "failed"

5. Mock Avatar URL:
   - Return something like fmt.Sprintf("https://avatars.example.com/%s.png", jobID)

6. Keep It Simple:
   - Synchronous processing is fine
   - Basic error handling is sufficient
   - Focus on the API integration


Content Moderation API:

POST /api/v1/moderate-content
Headers: Authorization: Bearer <token>
Body: {
  "content": "description of the generated avatar",
  "user_id": "user123"
}

Response: {
  "approved": true,
  "reason": "Content appears safe"
}
*/

package main

import (
	"time"
)

// ModerationResponse represents the response from the content moderation API
type ModerationResponse struct {
	IsApproved bool   `json:"is_approved"`
	Reason     string `json:"reason,omitempty"`
}

// AvatarJob represents an avatar generation job
type AvatarJob struct {
	ID           string    `json:"id"`
	UserID       string    `json:"user_id"`
	Status       string    `json:"status"` // pending, completed, failed, rejected
	InputData    string    `json:"input_data"`
	OutputURL    *string   `json:"output_url,omitempty"`
	CreatedAt    time.Time `json:"created_at"`
	ErrorMessage *string   `json:"error_message,omitempty"`
}

// NewAvatarJob creates a new avatar job with default values
func NewAvatarJob(id, userID, status, inputData string) *AvatarJob {
	return &AvatarJob{
		ID:        id,
		UserID:    userID,
		Status:    status,
		InputData: inputData,
		CreatedAt: time.Now(),
	}
}

// AvatarProcessingService handles avatar generation and moderation
type AvatarProcessingService struct {
	moderationAPIURL string
	apiToken         string
	// TODO: Add storage for jobs and HTTP client
}

// NewAvatarProcessingService creates a new avatar processing service
func NewAvatarProcessingService(moderationAPIURL, apiToken string) *AvatarProcessingService {
	return &AvatarProcessingService{
		moderationAPIURL: moderationAPIURL,
		apiToken:         apiToken,
		// TODO: Initialize your storage, HTTP client, etc.
	}
}

// SubmitJob submits a new avatar generation job and processes it synchronously
//
// Args:
//
//	userID: ID of the user requesting the avatar
//	inputData: User's avatar generation prompt/description
//
// Returns:
//
//	*AvatarJob: The completed job object
//	error: Any error that occurred during processing
//
// Should:
// 1. Create a new job with unique ID
// 2. Generate a mock avatar URL
// 3. Call moderation API
// 4. Update job status based on moderation result
// 5. Store and return the job
func (s *AvatarProcessingService) SubmitJob(userID, inputData string) (*AvatarJob, error) {
	// TODO: Implement job creation and full processing
	return nil, nil
}

// GetJobStatus retrieves the current status of a job
//
// Args:
//
//	jobID: ID of the job to check
//
// Returns:
//
//	*AvatarJob: The job object if found, nil otherwise
//	error: Any error that occurred during retrieval
func (s *AvatarProcessingService) GetJobStatus(jobID string) (*AvatarJob, error) {
	// TODO: Implement job retrieval from storage
	return nil, nil
}

// CallModerationAPI calls the content moderation API to check if avatar passes guidelines
//
// Args:
//
//	content: Description of the generated avatar
//	userID: ID of the user who requested the avatar
//
// Returns:
//
//	*ModerationResponse: Moderation result
//	error: Any error that occurred during API call
//
// Should:
// - Make HTTP POST request to moderation API
// - Handle timeouts and basic errors
// - Parse response into ModerationResponse struct
// - Optional: Add simple retry logic
func (s *AvatarProcessingService) CallModerationAPI(content, userID string) (*ModerationResponse, error) {
	// TODO: Implement HTTP client call with error handling
	return nil, nil
}

// generateMockAvatarURL generates a mock avatar URL (simulate avatar generation)
//
// Args:
//
//	prompt: User's avatar description
//
// Returns:
//
//	string: Mock URL to the generated avatar
func (s *AvatarProcessingService) generateMockAvatarURL(prompt string) string {
	// TODO: Return a mock URL like "https://avatars.example.com/avatar_123.png"
	return ""
}

// Example usage and testing
func main() {
	/*
		Example usage of the avatar processing service.
		You can use this to test your implementation.
	*/
	service := NewAvatarProcessingService(
		"https://api.example.com",
		"your-api-token-here",
	)

	// Submit a job
	job, err := service.SubmitJob("user123", "A friendly robot avatar with blue eyes")
	if err != nil {
		panic(err)
	}
	println("Job submitted:", job.ID, "Status:", job.Status)

	// Check status
	retrievedJob, err := service.GetJobStatus(job.ID)
	if err != nil {
		panic(err)
	}
	if retrievedJob != nil {
		println("Retrieved job status:", retrievedJob.Status)
	} else {
		println("Job not found")
	}
}
