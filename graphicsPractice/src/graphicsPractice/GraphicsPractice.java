package graphicsPractice;

import java.awt.*;
import javax.swing.*;

public class GraphicsPractice extends JFrame{
	private MyPanel panel = new MyPanel();
	
	public GraphicsPractice() {
		setTitle("예제");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setContentPane(panel);
		setSize(250, 200);
		setVisible(true);
		
	}
	
	class MyPanel extends JPanel{
		public void paintComponent(Graphics g) {
			super.paintComponent(g);
			g.setColor(Color.BLUE);
			g.drawRect(10, 10, 50, 50);
			g.fillRect(30, 30, 50, 50);
			g.setFont(new Font("Arial", Font.ITALIC, 30));
			g.drawString("Example", 30, 30);
			g.drawLine(10, 10, 50, 50);
			
			ImageIcon img = new ImageIcon("C:\\Users\\82104\\Desktop\\갤러리\\류수정.jpg");
			Image image = img.getImage();
			g.drawImage(image, 20, 20, this);
			//JLabel imgLabel = new JLabel(img);
			//add(imgLabel);
		}
	}
	
	public static void main(String[] args) {
		new GraphicsPractice();
	}

}