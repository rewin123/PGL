#version 120
uniform vec3 objectColor;
uniform vec3 lightColor;
uniform vec3 lightPos;
void main() {
	float ambientStrength = 0.1;
	vec3 ambient = ambientStrength * lightColor;

	vec3 result = ambient * objectColor;
    gl_FragColor = vec4( result, 1 );
}