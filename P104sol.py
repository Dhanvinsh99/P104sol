import cv2

sol = cv2.imread("solar-system.jpg")
cv2.putText(sol, "Sun", (20, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(sol, "Mercury", (120, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(sol, "Venus", (220, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(sol, "Earth", (320, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(sol, "Mars", (420, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(sol, "Jupiter", (500, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(sol, "Saturn", (800, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(sol, "Uranus", (1000, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(sol, "Neptune", (1150, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))



cv2.imshow("solar system", sol)
cv2.waitKey(0)