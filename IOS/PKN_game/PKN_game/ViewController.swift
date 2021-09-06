//
//  ViewController.swift
//  PKN_game
//
//  Created by Patryk Piwowarczyk on 03/09/2021.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var Paper: UIButton!
    
    @IBOutlet weak var scissors: UIButton!
    @IBOutlet weak var rock: UIButton!
    
    
    
    @IBOutlet weak var imageView: UIImageView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    
    
    var imageNum = 1
    
    
   

    let imagesArray = [ #imageLiteral(resourceName: "paper"), #imageLiteral(resourceName: "rock"), #imageLiteral(resourceName: "scissors") ]
    
    
    
    @IBAction func paperClicked(_ sender: UIButton) {
        
        imageView.image = imagesArray.first
        
        
    }
    
    
    
    @IBAction func rockClicked(_ sender: UIButton) {
        
        imageView.image = imagesArray[1]
        
    }
    
    
    @IBAction func scissorsClicked(_ sender: UIButton) {
        imageView.image = imagesArray.last
    }
    
// pisze sobie cos test test, test na Sziperd-branch, test 2
}

