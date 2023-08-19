## Potential Approaches 

### Traditional Web Server
- Limited resources
  - scalability issues
    - spinning up additional web server resources takes time (ECS)
- Error handling and retries have to be managed manually
- Resiliency must be handled within the application
  - conditional branching
  - sequencing

### serverless (lambda)
- Limited physical resources
- Hard limits on 
  - runtime duration
  - invocation payloads etc
- invocations, sequencing and branching needs to be managed
- not suitable for long-running workflows
- Retrying failed invocations and error handling is developer managed
