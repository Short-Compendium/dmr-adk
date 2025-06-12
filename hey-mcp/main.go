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
		"hey-you",
		"0.0.0",
	)

	// Add a tool
	sayHey := mcp.NewTool("say_hey",
		mcp.WithDescription("say hey to the person with the name <name>"),
		mcp.WithString("name",
			mcp.Required(),
			mcp.Description("the name of the person to greet"),
		),
	)

	// Add a tool handler
	s.AddTool(sayHey, sayHeyHandler)

	fmt.Println("MCP StreamableHTTP server is running on port 9090")

	//server.NewSSEServer(s, server.WithSSEEndpoint("/mcp")).Start(":8080")

	server.NewStreamableHTTPServer(s,
		server.WithEndpointPath("/mcp"),
	).Start(":9090")
	
}

func sayHeyHandler(ctx context.Context, request mcp.CallToolRequest) (*mcp.CallToolResult, error) {
	args := request.GetArguments()
	// Check if the name argument is provided
	if len(args) == 0 {
		return mcp.NewToolResultText("🤨 Hey, John Doe!"), nil
	}
	var content = ""
	if name, ok := args["name"]; ok {
		content = fmt.Sprintf("👋 Hey, %s!", name)
	} else {
		content = "🤔 Hey, John Doe!" // fallback if no name is provided
	}

	return mcp.NewToolResultText(content), nil
}
