"""
Avatar Processing Service - Complete Implementation

This service handles avatar generation requests by:
1. Creating jobs with unique IDs
2. Generating mock avatar URLs
3. Calling content moderation API
4. Returning processed results

INTERVIEW NOTE: Since the moderation API endpoint doesn't actually exist,
this implementation includes a mock mode (enabled by default) that simulates
API responses using keyword-based content filtering. In production, you would
set mock_mode=False to use the real API endpoint.
"""

from dataclasses import dataclass
from typing import Optional, Dict
from datetime import datetime
import uuid
import json
import urllib.request
import urllib.parse
import urllib.error


@dataclass
class ModerationResponse:
    is_approved: bool
    reason: Optional[str] = None


@dataclass
class AvatarJob:
    id: str
    user_id: str
    status: str  # pending, completed, failed, rejected
    input_data: str  # user's avatar prompt
    output_url: Optional[str] = None  # generated avatar URL
    created_at: datetime = None
    error_message: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()


class AvatarProcessingService:
    def __init__(self, moderation_api_url: str, api_token: str, mock_mode: bool = True):
        """
        Initialize the avatar processing service.
        
        Args:
            moderation_api_url: Base URL for the moderation API
            api_token: Bearer token for API authentication
            mock_mode: If True, simulates API responses instead of making real HTTP calls
        """
        self.moderation_api_url = moderation_api_url
        self.api_token = api_token
        self.mock_mode = mock_mode
        # In-memory storage for jobs
        self.jobs: Dict[str, AvatarJob] = {}

    def submit_job(self, user_id: str, input_data: str) -> AvatarJob:
        """
        Submit a new avatar generation job and process it synchronously.
        
        Args:
            user_id: ID of the user requesting the avatar
            input_data: User's avatar generation prompt/description
            
        Returns:
            AvatarJob: The completed job object
        """
        # Create a new job with unique ID
        job_id = str(uuid.uuid4())
        job = AvatarJob(
            id=job_id,
            user_id=user_id,
            status="pending",
            input_data=input_data
        )
        
        # Store the job
        self.jobs[job_id] = job
        
        try:
            # Generate mock avatar URL
            avatar_url = self._generate_mock_avatar_url(input_data)
            job.output_url = avatar_url
            
            # Call moderation API
            moderation_result = self.call_moderation_api(input_data, user_id)
            
            # Update job status based on moderation result
            if moderation_result.is_approved:
                job.status = "completed"
            else:
                job.status = "rejected"
                job.error_message = moderation_result.reason
                # Clear the avatar URL for rejected content
                job.output_url = None
                
        except Exception as e:
            # Handle any errors during processing
            job.status = "failed"
            job.error_message = str(e)
            job.output_url = None
        
        return job

    def get_job_status(self, job_id: str) -> Optional[AvatarJob]:
        """
        Retrieve the current status of a job.
        
        Args:
            job_id: ID of the job to check
            
        Returns:
            AvatarJob or None: The job object if found, None otherwise
        """
        return self.jobs.get(job_id)

    def call_moderation_api(self, content: str, user_id: str) -> ModerationResponse:
        """
        Call the content moderation API to check if avatar passes guidelines.
        
        Args:
            content: Description of the generated avatar
            user_id: ID of the user who requested the avatar
            
        Returns:
            ModerationResponse: Moderation result
        """
        # Use mock implementation if in mock mode
        if self.mock_mode:
            return self._mock_moderation_response(content, user_id)
        
        # Real API implementation
        try:
            # Construct the full API URL
            api_url = f"{self.moderation_api_url}/api/v1/moderate-content"
            
            # Prepare request payload
            payload = {
                "content": content,
                "user_id": user_id
            }
            
            # Prepare request data and headers
            data = json.dumps(payload).encode('utf-8')
            headers = {
                'Authorization': f'Bearer {self.api_token}',
                'Content-Type': 'application/json',
                'Content-Length': str(len(data))
            }
            
            # Create request object
            request = urllib.request.Request(api_url, data=data, headers=headers, method='POST')
            
            # Make HTTP POST request with timeout
            with urllib.request.urlopen(request, timeout=5) as response:
                response_data = response.read().decode('utf-8')
                data = json.loads(response_data)
            
            return ModerationResponse(
                is_approved=data.get("approved", False),
                reason=data.get("reason", "No reason provided")
            )
            
        except urllib.error.URLError as e:
            if hasattr(e, 'reason'):
                raise Exception(f"Moderation API request failed: {str(e.reason)}")
            else:
                raise Exception(f"Moderation API request failed: {str(e)}")
        except json.JSONDecodeError as e:
            raise Exception(f"Invalid response format from moderation API: {str(e)}")
        except Exception as e:
            raise Exception(f"Moderation API error: {str(e)}")

    def _mock_moderation_response(self, content: str, user_id: str) -> ModerationResponse:
        """
        Mock implementation of content moderation for demo purposes.
        Uses simple heuristics to simulate real moderation behavior.
        
        Args:
            content: Description of the generated avatar
            user_id: ID of the user who requested the avatar
            
        Returns:
            ModerationResponse: Simulated moderation result
        """
        # Define inappropriate keywords that would trigger rejection
        inappropriate_keywords = [
            'violent', 'violence', 'weapon', 'weapons', 'gun', 'knife', 'sword',
            'blood', 'bloody', 'gore', 'death', 'kill', 'murder',
            'hate', 'nazi', 'racist', 'terror', 'bomb',
            'nude', 'naked', 'sexual', 'porn', 'explicit',
            'drug', 'cocaine', 'marijuana', 'alcohol'
        ]
        
        # Convert content to lowercase for case-insensitive matching
        content_lower = content.lower()
        
        # Check for inappropriate content
        found_inappropriate = []
        for keyword in inappropriate_keywords:
            if keyword in content_lower:
                found_inappropriate.append(keyword)
        
        # Additional checks for edge cases
        if len(content.strip()) == 0:
            return ModerationResponse(
                is_approved=False,
                reason="Content cannot be empty"
            )
        
        if len(content) > 1000:
            return ModerationResponse(
                is_approved=False,
                reason="Content exceeds maximum length limit"
            )
        
        # Return result based on findings
        if found_inappropriate:
            return ModerationResponse(
                is_approved=False,
                reason=f"Content contains inappropriate material: {', '.join(found_inappropriate[:3])}"
            )
        else:
            return ModerationResponse(
                is_approved=True,
                reason="Content appears safe and appropriate"
            )

    def _generate_mock_avatar_url(self, prompt: str) -> str:
        """
        Generate a mock avatar URL (simulate avatar generation).
        
        Args:
            prompt: User's avatar description
            
        Returns:
            str: Mock URL to the generated avatar
        """
        # Generate a unique identifier based on prompt hash and timestamp
        unique_id = str(hash(prompt + str(datetime.now().timestamp())))[-8:]
        return f"https://avatars.example.com/avatar_{unique_id}.png"


# Example usage and testing
def main():
    """
    Example usage of the avatar processing service.
    Demonstrates both approved and rejected content scenarios.
    """
    # Initialize service in mock mode (since real API doesn't exist)
    print("=== Avatar Processing Service Demo ===")
    print("Note: Running in mock mode since real moderation API is not available")
    print()
    
    service = AvatarProcessingService(
        moderation_api_url="https://api.example.com",
        api_token="your-api-token-here",
        mock_mode=True  # Explicitly showing mock mode for demo
    )
    
    # Test Case 1: Appropriate content (should be approved)
    print("TEST 1: Submitting appropriate avatar request...")
    job1 = service.submit_job("user123", "A friendly robot avatar with blue eyes and a smile")
    print(f"Job ID: {job1.id}")
    print(f"Status: {job1.status}")
    print(f"Avatar URL: {job1.output_url}")
    if job1.error_message:
        print(f"Error: {job1.error_message}")
    print()
    
    # Test Case 2: Inappropriate content (should be rejected)
    print("TEST 2: Submitting inappropriate avatar request...")
    job2 = service.submit_job("user456", "Violent avatar with weapons and blood")
    print(f"Job ID: {job2.id}")
    print(f"Status: {job2.status}")
    print(f"Avatar URL: {job2.output_url}")
    if job2.error_message:
        print(f"Rejection reason: {job2.error_message}")
    print()
    
    # Test Case 3: Edge case - empty content
    print("TEST 3: Submitting empty content...")
    job3 = service.submit_job("user789", "")
    print(f"Job ID: {job3.id}")
    print(f"Status: {job3.status}")
    print(f"Avatar URL: {job3.output_url}")
    if job3.error_message:
        print(f"Rejection reason: {job3.error_message}")
    print()
    
    # Test Case 4: Job status retrieval
    print("TEST 4: Retrieving job status...")
    retrieved_job = service.get_job_status(job1.id)
    if retrieved_job:
        print(f"Retrieved job {job1.id}: {retrieved_job.status}")
        print(f"Created at: {retrieved_job.created_at}")
    else:
        print("Job not found")
    print()
    
    # Show summary of all jobs
    print("=== JOB SUMMARY ===")
    for job_id, job in service.jobs.items():
        print(f"Job {job_id[:8]}...: {job.status} - '{job.input_data[:50]}...'")
    
    print(f"\nTotal jobs processed: {len(service.jobs)}")
    
    # Demo: How to switch to real API mode
    print("\n=== PRODUCTION USAGE ===")
    print("To use with real API, initialize with mock_mode=False:")
    print("service = AvatarProcessingService(")
    print("    moderation_api_url='https://real-api.com',")
    print("    api_token='real-token',")
    print("    mock_mode=False")
    print(")")


if __name__ == "__main__":
    main() 