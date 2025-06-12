package main

import (
	"context"
	"fmt"

	"github.com/mark3labs/mcp-go/mcp"
	"github.com/mark3labs/mcp-go/server"
)

func main() {
	// Create MCP server
	s := server.NewMCPServer(
		"hello-you",
		"0.0.0",
	)

	// Add a tool
	sayHello := mcp.NewTool("say_hello",
		mcp.WithDescription("say hello to the person with the name <name>"),
		mcp.WithString("name",
			mcp.Required(),
			mcp.Description("the name of the person to greet"),
		),
	)

	// Add a tool handler
	s.AddTool(sayHello, sayHelloHandler)

	fmt.Println("MCP SSE server is running on port 8080")

	server.NewSSEServer(s, server.WithSSEEndpoint("/mcp")).Start(":8080")

	/*
	server.NewStreamableHTTPServer(s,
		server.WithEndpointPath("/mcp"),
	).Start(":8080")
	*/
}

func sayHelloHandler(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	args := request.GetArguments()
	// Check if the name argument is provided
	if len(args) == 0 {
		return mcp.NewToolResultText("🤨 Hello, John Doe!"), nil
	}
	var content = ""
	if name, ok := args["name"]; ok {
		content = fmt.Sprintf("🙂 Hello, %s!", name)
	} else {
		content = "🤔 Hello, John Doe!" // fallback if no name is provided
	}

	return mcp.NewToolResultText(content), nil
}
