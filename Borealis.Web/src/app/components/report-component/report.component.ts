import { Component, OnInit } from '@angular/core';
import { ReportService } from 'src/app/services/report.service';

@Component({
    selector: 'report',
    templateUrl: './report.component.html',
    styleUrls: ['./report.component.scss']
})
export class ReportComponent implements OnInit {

    constructor(private reportService: ReportService) { }

    ngOnInit(): void {
    }

    downloadReport(): void {
        this.reportService.getReport().subscribe(
            res => {
                var blob = this.dataURItoBlob(res.file);
                let url = window.URL.createObjectURL(blob);
                let a = document.createElement('a');
                document.body.appendChild(a);
                a.setAttribute('style', 'display: none');
                a.href = url;
                a.download = "report.csv";
                a.click();
                window.URL.revokeObjectURL(url);
                a.remove();
            }
        );
    }

    dataURItoBlob(dataURI) {
        const byteString = window.atob(dataURI);
        const arrayBuffer = new ArrayBuffer(byteString.length);
        const int8Array = new Uint8Array(arrayBuffer);
        for (let i = 0; i < byteString.length; i++) {
          int8Array[i] = byteString.charCodeAt(i);
        }
        const blob = new Blob([int8Array], { type: 'image/png' });    
        return blob;
     }

}
